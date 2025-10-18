from random import choice
match __name__:
    case "__main__":
        import hangman_variables as variables
    case _:
        import library.hangman_variables as variables

def start():
    print("Welcome to Hangman Game!")
    print("Try to guess the word before the hangman appears!")
    print("You have 6 attempts to guess the word.")
    print("Let's start the game!")
    print()

def difficulty(difficulty_level):
    match difficulty_level:
        case "easy":
            secret_word = choice(variables.easy)
            return secret_word
        case "medium":
            secret_word = choice(variables.medium)
            return secret_word
        case "hard":
            secret_word = choice(variables.hard)
            return secret_word
        case _:
            return "Error: Invalid difficulty level."

def hangman(secret_word):
    guessed_letters = ""
    attempts = 6
    while attempts > 0:
        print(variables.hangman_art[attempts])
        print("Word: " + "".join([letter if letter in guessed_letters else "_" for letter in secret_word]))
        guess = input("Guess a letter: ").lower()
        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in secret_word:
            guessed_letters += guess
            if "".join([letter if letter in guessed_letters else "_" for letter in secret_word]) == secret_word:
                print("Word: " + "".join([letter if letter in guessed_letters else "_" for letter in secret_word]))
                print("You guessed the word! Congratulations!")
                break
        else:
            attempts -= 1
            print(f"Incorrect guess. You have {attempts} attempts left.")
    if attempts == 0:
        print(f"You lost! The word was: {secret_word}")

def help():
    print()
    print("This module contains the functions for the hangman game.")
    print("There are 3 functions in this module:")
    print("start(): This function prints a message that welcomes the user to the game.")
    print("difficulty(difficulty_level): This function takes a difficulty level as an argument and returns a random word from the corresponding list found in the hangman_variables module.")
    print("hangman(secret_word): This function takes a secret word that the difficulty function returns as an argument and runs the game.")
    print("help(): This function prints a message that explains how to use the module.")
    print()

match __name__:
    case "__main__":
        help()
    case _:
        pass