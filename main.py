def update_game_state(secret_word: str,
                      guessed_letters: list[str],
                      guess: str,
                      lives: int) -> tuple[list[str], int]:
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