# Lab 4: Word Game (Hangman)

## Description

This repository contains a Python implementation of the classic Hangman word-guessing game. The project demonstrates clean code architecture with separated logic and user interface layers, comprehensive test coverage, and iterative development practices. It was developed as part of a laboratory assignment, incorporating AI-assisted coding techniques.

The game allows players to guess letters to uncover a hidden word, with a maximum of 6 incorrect guesses allowed. The implementation includes features such as case-insensitive input, duplicate guess handling, and replay functionality.

## Features

- **Core Gameplay**: Random word selection from a predefined list, letter-by-letter guessing with immediate feedback
- **Input Validation**: Accepts only single alphabetic characters, handles duplicates gracefully
- **Game States**: Tracks ongoing, won, and lost states with appropriate win/loss detection
- **User Interface**: Command-line interface with clear display of game progress
- **Replay Support**: Option to play multiple rounds without restarting the program
- **Modular Design**: Separated logic layer (game state management) from UI layer (display and input)
- **Comprehensive Testing**: Full test suite using pytest with parameterized tests and edge case coverage

## Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Setup

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/lab4-word-gamepleasework.git
   cd lab4-word-gamepleasework
   ```

2. Install dependencies (if any):
   ```
   pip install -r requirements.txt
   ```
   Note: This project uses only standard library modules, so no external dependencies are required.

## Usage

Run the game from the command line:

```
python main.py
```

The game will:
1. Select a random word from the predefined list
2. Display the word as underscores (e.g., "_ _ _ _ _")
3. Prompt for letter guesses
4. Update the display and track incorrect guesses
5. Continue until the word is guessed or maximum wrong guesses are reached
6. Offer to play again

### Example Gameplay

```
🎮 HANGMAN 🎮
I'm thinking of a 6-letter word.

==================================================
Word:     _ _ _ _ _ _
Guessed:  (none)
Errors:   0/6
==================================================

Guess a letter: p

==================================================
Word:     p _ _ _ _ _
Guessed:  p
Errors:   0/6
==================================================
```

## Testing

The project includes a comprehensive test suite using pytest. To run the tests:

```
python -m pytest test_main.py
```

The test suite covers:
- Core game logic functions (`update_game_state`, `build_display_word`, `check_win_condition`)
- Game class behavior and state transitions
- Edge cases including duplicate guesses, invalid input, and win/loss conditions

## Project Structure

```
lab4-word-gamepleasework/
├── main.py              # Main game implementation with logic and UI layers
├── test_main.py         # Comprehensive test suite
├── REPORT.md            # Personal development report
├── JOURNAL.md           # Development interaction log
├── README.md            # This file
└── My original thinking/
    └── MY_NOTED.md      # Initial design notes and requirements
```

## Development Notes

This project was developed using GitHub Copilot as an AI coding assistant. The development process involved:
- Iterative implementation with AI-generated code suggestions
- Focus on clean architecture and separation of concerns
- Comprehensive testing to ensure correctness
- Documentation of all interactions and changes in JOURNAL.md

Key design decisions:
- Character-by-character word building instead of string replacement
- Case-insensitive processing throughout
- Avoidance of infinite loops in favor of structured game flow
- Modular function design for testability

## Contributing

This is an educational project for a laboratory assignment. For suggestions or improvements, please create an issue in the repository.

## License

This project is released under the MIT License. See LICENSE file for details (if applicable).</content>
<parameter name="filePath">c:\Users\polak\Documents\GitHub\lab4-word-gamepleasework\README.md