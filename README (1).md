# Hangman Game - Save the Prisoner

A command-line word-guessing game written in Python. An evil wizard has captured a prisoner, and the only way to free them is to guess the secret word. Every wrong guess brings the prisoner closer to their fate.

## How to Play

1. The game randomly picks a secret word from a list.
2. The word is shown as underscores, one for each letter (for example `_ _ _ _ _ _`).
3. Guess one letter at a time.
4. Correct guesses are revealed in the word. Wrong guesses count against you.
5. Guess the whole word before you run out of attempts (6 by default) to free the prisoner.

## Features

- Random word selection from a list
- Underscore display that updates with each correct guess
- Limited number of wrong guesses
- Input validation (single letters only, no repeated guesses)
- Display of all letters guessed so far
- Option to play again after each round

## Concepts Used

- Loops (`while`, `for`, and `while...else`)
- Conditionals (`if` / `elif` / `else`)
- The `random` module
- Lists
- String manipulation
- Functions

## Requirements

- Python 3.6 or higher
- No external libraries needed

## How to Run

```bash
git clone https://github.com/<your-username>/hangman-game.git
cd hangman-game
python hangman.py
```

On some systems you may need to use `python3 hangman.py` instead.

## Example Gameplay

```
==================================================
  WELCOME TO HANGMAN - Save the Prisoner!
==================================================
The wizard has trapped a prisoner behind a 6-letter word.
You have 6 wrong guesses before it's too late.

Word: _ _ _ _ _ _
Wrong guesses: 0/6
Guess a letter: a
Wrong! 'a' is not in the word. 5 attempt(s) left.
```

## Customization

At the top of `hangman.py` you can change:

- `WORD_LIST` to add or replace the possible secret words
- `MAX_ATTEMPTS` to make the game easier or harder

## Project Structure

```
hangman-game/
├── hangman.py     # Game code
├── README.md      # Project documentation
└── .gitignore     # Files Git should ignore
```

## Author

Gaurav
