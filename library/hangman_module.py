# Hangman Module Game
# This is a module that contains the functions and core game logic for the hangman game.
# The module is imported by the main script and used to run the game.

# First I import the choice function from the random module.
from random import choice

# Then I check if the module is being imported or run as the main script.
match __name__:
#    If the module is being run as the main script, I import the hangman_variables module.
    case "__main__":
        import hangman_variables as variables
#    If the module is being imported, I import the hangman_variables module.
    case _:
        import library.hangman_variables as variables

# Then I define the start() function that prints a message that welcomes the user to the game.
def start():
    print("Welcome to Hangman Game!")
    print("Try to guess the word before the hangman appears!")
    print("You have 6 attempts to guess the word.")
    print("Let's start the game!")
    print()

# Then I define the difficulty() function that takes a difficulty level as an argument and returns a random word from the corresponding list found in the hangman_variables module.
def difficulty(difficulty_level):
    match difficulty_level:
#        If the difficulty level is easy, I return a random word from the easy list in the hangman_variables module.
        case "easy":
            secret_word = choice(variables.easy)
            return secret_word
#        If the difficulty level is medium, I return a random word from the medium list in the hangman_variables module.
        case "medium":
            secret_word = choice(variables.medium)
            return secret_word
#        If the difficulty level is hard, I return a random word from the hard list in the hangman_variables module.
        case "hard":
            secret_word = choice(variables.hard)
            return secret_word
#        If the difficulty level is invalid, I return an error message.
        case _:
            return "Error: Invalid difficulty level."

# Then I define the hangman() function that takes a secret word as an argument and runs the core game logic.
def hangman(secret_word):
#    I initialize the guessed_letters variable to an empty string and the attempts variable to 6.
    guessed_letters = ""
    attempts = 6
#    I start a while loop that runs while the attempts variable is greater than 0.
    while attempts > 0:
#        I print the ASCII art for the hangman game from the hangman_variables module.
        print(variables.hangman_art[attempts])
#        I print the word that the user has guessed so far.
        print("Word: " + "".join([letter if letter in guessed_letters else "_" for letter in secret_word]))
#        I ask the user to guess a letter.
        guess = input("Guess a letter: ").lower()
#        I check if the guess is already in the guessed_letters variable.
        if guess in guessed_letters:
#            If it is, then the program will print "You already guessed that letter".
            print("You already guessed that letter.")
#        If the guess is not in the guessed_letters variable, I check if it is in the secret_word variable.
        elif guess in secret_word:
#            If it is, I add it to the guessed_letters variable.
            guessed_letters += guess
#            I check if the guessed_letters variable is equal to the secret_word variable.
            if "".join([letter if letter in guessed_letters else "_" for letter in secret_word]) == secret_word:
#                If it is, then the program will print the word and "You guessed the word! Congratulations!"
                print("Word: " + "".join([letter if letter in guessed_letters else "_" for letter in secret_word]))
                print("You guessed the word! Congratulations!")
#                then the program will break out of the loop.
                break
#            If it is not, then the program will print "Correct guess!"
            else:
                print("Correct guess!")
#        If the guess is not in the secret_word variable, I subtract 1 from the attempts variable and print "Incorrect guess. You have {attempts} attempts left."
        else:
            attempts -= 1
            print(f"Incorrect guess. You have {attempts} attempts left.")
#    If the attempts variable is 0, then the program will print "You lost! The word was: {secret_word}"
    if attempts == 0:
        print(f"You lost! The word was: {secret_word}")

# Then I define the help() function that prints a message that explains how to use the module.
def help():
    print()
    print("This module contains the functions for the hangman game.")
    print("There are 4 functions in this module:")
    print("start(): This function prints a message that welcomes the user to the game.")
    print("difficulty(difficulty_level): This function takes a difficulty level as an argument and returns a random word from the corresponding list found in the hangman_variables module.")
    print("hangman(secret_word): This function takes a secret word that the difficulty function returns as an argument and runs the game.")
    print("help(): This function prints a message that explains how to use the module.")
    print()

# Then I check if the module is being imported or run as the main script.
match __name__:
#    If the module is being run as the main script, I call the help() function to print a message that explains how to use the module.
    case "__main__":
        help()
#    If the module is being imported, I do nothing.
    case _:
        pass