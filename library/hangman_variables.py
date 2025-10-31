# Hangman Variables
# This is a module that contains the variables for the hangman game implemented in Python.
# The module is imported by the hangman_module module, which is used to determine the words for the game and the hangman ASCII art.

"""
This module contains the variables for the hangman game.

There are 4 variables in this module:

easy: A list of easy words for the user to guess in the hangman game.
medium: A list of medium words for the user to guess in the hangman game.
hard: A list of hard words for the user to guess in the hangman game.
hangman_art: A list of ASCII art for the hangman game.
"""

# First I create a list of easy words for the user to guess in the hangman game.
easy = ["code", "game", "python", "list", "loop", "string", "variable", "function", "class", "import"]
# Then I create a list of medium words for the user to guess in the hangman game.
medium = ["program", "algorithm", "database", "software", "hardware", "browser", "network", "keyboard", "monitor", "terminal"]
# Then I create a list of hard words for the user to guess in the hangman game.
hard = ["javascript", "framework", "repository", "encryption", "artificial", "blockchain", "cybersecurity", "machinelearning"]

# Then I create a list of ASCII art for the hangman game.
hangman_art = ["""

    +---+
    |   |
    0   |
   /|\  |
   / \  |
        |
    =========""", """

    +---+
    |   |
    0   |
   /|\  |
   /    |
        |
    =========""", """

    +---+
    |   |
    0   |
   /|\  |
        |
        |
    =========""", """

    +---+
    |   |
    0   |
   /|   |
        |
        |
    =========""", """

    +---+
    |   |
    0   |
    |   |
        |
        |
    =========""", """

    +---+
    |   |
    0   |
        |
        |
        |
    =========""", """

    +---+
    |   |
        |
        |
        |
        |
    ========="""]

# Then I define the help() function that prints a message that explains how to use the module.
def help():
    """
    This function prints a message that explains how to use the module.
    It lists the variables in the module and explains what they are used for.
    """
    print()
    print("This module contains the variables for the hangman game.")
    print("There are 4 variables in this module:")
    print("easy: A list of easy words for the user to guess in the hangman game.")
    print("medium: A list of medium words for the user to guess in the hangman game.")
    print("hard: A list of hard words for the user to guess in the hangman game.")
    print("hangman_art: A list of ASCII art for the hangman game.")
    print()

# Then I check if the module is being imported or run as the main script.
match __name__:
#    If the module is being run as the main script, I call the help() function to print a message that explains how to use the module.
    case "__main__":
        help()
#    If the module is being imported, I do nothing.
    case _:
        pass