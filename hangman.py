# Hangman Game
# By Amnoor Brar
# This is a classic word-guessing game implemented in Python. Test your vocabulary skills as you try to solve the puzzle before the hangman appears!
# This is a module-based project that uses the hangman_module and hangman_variables modules to implement the game.
# The hangman_module module contains the functions for the game, and the hangman_variables module contains the variables for the game.
# The main script imports the hangman_module module and uses it to run the game.
# The main module imports the hangman_variables module and uses it to get the words for the game.

# First I import the hangman_module module for the core game logic.
import library.hangman_module as hangman

# Then I call the start() function from the hangman_module module to print a welcome message.
hangman.start()

is_running = True
while is_running:
#    Then create a while loop that prompts the user to choose a valid difficulty level.
    is_valid_difficulty_choice = True
    while is_valid_difficulty_choice:
#        Then I ask the user to choose a difficulty level.
        inputed_difficulty = input("Choose a difficulty level (easy, medium, hard): ")
#        Then I call the difficulty() function from the hangman_module module to get a random word for the chosen difficulty level.
        secret_word = hangman.difficulty(inputed_difficulty)
#        Then I check if the secret_word is valid or not.
        match secret_word:
#            If the secret_word is not valid, I print an error message and set is_valid_choice to True so that the loop will continue until the user chooses a valid difficulty level.
            case "Error: Invalid difficulty level.":
                print(secret_word)
                is_valid_difficulty_choice = True
#            If the secret_word is valid, then I will set is_valid_choice to False to end the loop.
            case _:
                is_valid_difficulty_choice = False

#    Then I call the hangman() function from the hangman_module module to run the game.
    hangman.hangman(secret_word)

#    Then I create a while loop that prompts the user to choose to play again or not.
    is_valid_boolen_choice = True
    while is_valid_boolen_choice:
#        Then I assign a variable to the user's input.
        inputed_boolen = input("Do you want to play again? (yes(y) or no(n)): ").lower().strip()
#        Then I check if the user's input is valid or not.
        match inputed_boolen:
#            If the user's inputed "yes" or "y", then I set the is_valid_boolen_choice variable to False and set the is_running variable to True to start a new game.
            case "yes" | "y":
                is_valid_boolen_choice = False
                is_running = True
                print()
#            If the user's inputed "no" or "n", then I set the is_valid_boolen_choice variable to False, set the is_running variable to False, and print "Thanks for playing! Goodbye!" then end the game.
            case "no" | "n":
                is_valid_boolen_choice = False
                is_running = False
                print("Thanks for playing! Goodbye!")
#            If the user's input is not valid, then I print "Invalid input. Please enter yes(y) or no(n)." and set is_valid_boolen_choice to True so that the loop will continue until the user chooses a valid input.
            case _:
                print("Invalid input. Please enter yes(y) or no(n).")
                is_valid_boolen_choice = True