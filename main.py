"""Hangman game with separated logic and UI layers."""

import random


# ============================================================================
# CONSTANTS
# ============================================================================

WORD_LIST = [
    "python", "hangman", "programming", "algorithm", "database",
    "function", "variable", "syntax", "compiler", "debugger"
]

MAX_WRONG_GUESSES = 6


# ============================================================================
# LOGIC LAYER (Game State & Core Logic)
# ============================================================================

def update_game_state(secret_word: str,
                      guessed_letters: list[str],
                      guess: str,
                      lives: int) -> tuple[list[str], int]:
    """Process *guess* against *secret_word*.

    The returned tuple holds an updated list of letters that
    have been seen so far and the new lives count.  The
    implementation is case‑insensitive and treats duplicate
    guesses as a no‑op (they neither cost a life nor are added
    again).

    Arguments:
        secret_word: the word the player is trying to uncover.
        guessed_letters: previous guesses (lowercase preferred).
        guess: single-character string supplied by the player.
        lives: number of remaining incorrect guesses allowed.

    Raises:
        ValueError: if *guess* is not a single alphabetic
            character.
    """
    # Validate input
    if not isinstance(guess, str) or len(guess) != 1 or not guess.isalpha():
        raise ValueError("Guess must be a single alphabetic character")
    
    guess_lower = guess.lower()
    secret_lower = secret_word.lower()
    
    # Check for duplicate guesses (case-insensitive)
    if guess_lower in [g.lower() for g in guessed_letters]:
        return guessed_letters, lives  # No change for duplicate
    
    # Update guessed letters
    new_guessed_letters = guessed_letters + [guess_lower]
    
    # Update lives only if guess is wrong
    new_lives = lives - 1 if guess_lower not in secret_lower else lives
    
    return new_guessed_letters, new_lives


def build_display_word(secret_word: str, guessed_letters: list[str]) -> str:
    """Build display representation of word with guessed letters revealed.
    
    Uses character-by-character building instead of string replacement.
    Unguessed letters appear as underscores.
    """
    secret_lower = secret_word.lower()
    guessed_set = set(g.lower() for g in guessed_letters)
    
    display = []
    for char in secret_lower:
        if char in guessed_set:
            display.append(char)
        else:
            display.append("_")
    
    return " ".join(display)


def check_win_condition(secret_word: str, guessed_letters: list[str]) -> bool:
    """Check if all letters of the word have been guessed."""
    secret_set = set(secret_word.lower())
    guessed_set = set(g.lower() for g in guessed_letters)
    return secret_set.issubset(guessed_set)


class Game:
    """Encapsulates all game state and logic."""
    
    def __init__(self, secret_word: str):
        self.secret_word = secret_word.lower()
        self.guessed_letters = []
        self.wrong_guesses = 0
        self.state = "ongoing"  # ongoing, won, lost
    
    def play_turn(self, guess: str) -> None:
        """Process a single guess and update game state.
        
        Raises:
            ValueError: if guess is invalid or game is already over.
        """
        if self.state != "ongoing":
            raise ValueError("Game is already over")
        
        old_guessed = self.guessed_letters
        self.guessed_letters, lives_remaining = update_game_state(
            self.secret_word, self.guessed_letters, guess, 
            MAX_WRONG_GUESSES - self.wrong_guesses
        )
        
        # Update wrong guess counter
        if len(self.guessed_letters) > len(old_guessed):
            wrong_before = self.wrong_guesses
            self.wrong_guesses = MAX_WRONG_GUESSES - lives_remaining
        
        # Check win/loss conditions
        if check_win_condition(self.secret_word, self.guessed_letters):
            self.state = "won"
        elif self.wrong_guesses >= MAX_WRONG_GUESSES:
            self.state = "lost"
    
    def is_game_over(self) -> bool:
        return self.state in ["won", "lost"]
    
    def has_won(self) -> bool:
        return self.state == "won"
    
    def has_lost(self) -> bool:
        return self.state == "lost"
    
    def get_display_word(self) -> str:
        return build_display_word(self.secret_word, self.guessed_letters)
    
    def get_status(self) -> dict:
        """Return current game status for UI."""
        return {
            "display": self.get_display_word(),
            "guessed": self.guessed_letters,
            "wrong_count": self.wrong_guesses,
            "max_wrong": MAX_WRONG_GUESSES,
            "state": self.state
        }


# ============================================================================
# UI LAYER (Display Functions)
# ============================================================================

def display_game(game: Game) -> None:
    """Display current game state."""
    status = game.get_status()
    print("\n" + "="*50)
    print(f"Word:     {status['display']}")
    print(f"Guessed:  {', '.join(status['guessed']) if status['guessed'] else '(none)'}")
    print(f"Errors:   {status['wrong_count']}/{status['max_wrong']}")
    print("="*50)


def display_result(game: Game) -> None:
    """Display game result."""
    if game.has_won():
        print(f"\n✓ YOU WON! The word was: {game.secret_word.upper()}")
    else:
        print(f"\n✗ YOU LOST! The word was: {game.secret_word.upper()}")


def get_player_guess() -> str:
    """Get and validate a single letter guess from player."""
    while True:
        guess = input("\nGuess a letter: ").strip()
        if guess.isalpha() and len(guess) == 1:
            return guess
        print("Please enter a single letter.")


# ============================================================================
# MAIN GAME LOOP
# ============================================================================

def run_game() -> bool:
    """Run a single game session. Return True if player wants to play again."""
    secret_word = random.choice(WORD_LIST)
    game = Game(secret_word)
    
    print("\n🎮 HANGMAN 🎮")
    print(f"I'm thinking of a {len(secret_word)}-letter word.")
    
    while not game.is_game_over():
        display_game(game)
        guess = get_player_guess()
        
        try:
            game.play_turn(guess)
        except ValueError as e:
            print(f"Error: {e}")
    
    display_result(game)
    
    response = input("\nPlay again? (y/n): ").strip().lower()
    return response == "y"


def main() -> None:
    """Entry point. Runs games until player quits."""
    play = True
    while play:
        play = run_game()
    print("\nThanks for playing! Goodbye.")


if __name__ == "__main__":
    main()