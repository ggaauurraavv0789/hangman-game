"""
Hangman Game - "Save the Prisoner"
------------------------------------
A classic word-guessing game where the player must guess a secret word
letter by letter before running out of attempts.

Concepts used: loops, conditionals, the random module, lists, and
string manipulation.

Author: <Your Name Here>
"""

import random


# ---------------------------------------------------------
# List of words the game can randomly choose from
# ---------------------------------------------------------
WORD_LIST = [
    "python", "wizard", "kingdom", "prisoner", "dragon",
    "castle", "sword", "magic", "hangman", "treasure"
]

MAX_ATTEMPTS = 6  # Number of wrong guesses allowed


def choose_word(word_list):
    """Randomly select a word from the given list."""
    return random.choice(word_list).lower()


def display_word(word, guessed_letters):
    """
    Return a string showing correctly guessed letters
    and underscores for the rest.
    """
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()


def get_guess(guessed_letters):
    """Prompt the player for a single, valid, new letter guess."""
    while True:
        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
        elif guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.")
        else:
            return guess


def play_hangman():
    """Main game loop."""
    secret_word = choose_word(WORD_LIST)
    guessed_letters = []
    wrong_guesses = 0

    print("=" * 50)
    print("  WELCOME TO HANGMAN - Save the Prisoner!")
    print("=" * 50)
    print(f"The wizard has trapped a prisoner behind a "
          f"{len(secret_word)}-letter word.")
    print(f"You have {MAX_ATTEMPTS} wrong guesses before it's too late.\n")

    while wrong_guesses < MAX_ATTEMPTS:
        print(f"\nWord: {display_word(secret_word, guessed_letters)}")
        print(f"Wrong guesses: {wrong_guesses}/{MAX_ATTEMPTS}")
        if guessed_letters:
            print(f"Guessed letters: {', '.join(guessed_letters)}")

        guess = get_guess(guessed_letters)
        guessed_letters.append(guess)

        if guess in secret_word:
            print(f"Correct! '{guess}' is in the word.")
        else:
            wrong_guesses += 1
            remaining = MAX_ATTEMPTS - wrong_guesses
            print(f"Wrong! '{guess}' is not in the word. "
                  f"{remaining} attempt(s) left.")

        # Check win condition: every letter in the word has been guessed
        if all(letter in guessed_letters for letter in secret_word):
            print(f"\nCongratulations! You guessed it: '{secret_word}'")
            print("The prisoner is FREE! You saved the day! 🎉")
            break
    else:
        # This 'else' belongs to the while loop; runs if loop ends
        # WITHOUT hitting 'break' (i.e., player ran out of attempts)
        print(f"\nOut of attempts! The word was '{secret_word}'.")
        print("The prisoner's fate is sealed... Game Over.")


def play_again():
    """Ask the player if they'd like another round."""
    choice = input("\nWould you like to play again? (y/n): ").lower().strip()
    return choice.startswith("y")


if __name__ == "__main__":
    keep_playing = True
    while keep_playing:
        play_hangman()
        keep_playing = play_again()

    print("\nThanks for playing Hangman! Goodbye.")
