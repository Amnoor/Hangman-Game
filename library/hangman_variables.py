easy = ["code", "game", "python", "list", "loop", "string", "variable", "function", "class", "import"]
medium = ["program", "algorithm", "database", "software", "hardware", "browser", "network", "keyboard", "monitor", "terminal"]
hard = ["javascript", "framework", "repository", "encryption", "artificial", "blockchain", "cybersecurity", "machinelearning"]

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

def help():
    print()
    print("This module contains the variables for the hangman game.")
    print("There are 4 variables in this module:")
    print("easy: A list of easy words for the user to guess in the hangman game.")
    print("medium: A list of medium words for the user to guess in the hangman game.")
    print("hard: A list of hard words for the user to guess in the hangman game.")
    print("hangman_art: A list of ASCII art for the hangman game.")
    print()

match __name__:
    case "__main__":
        help()
    case _:
        pass