import library.hangman_module as hangman
hangman.start()

is_valid_choice = True
while is_valid_choice:
    inputed_difficulty = input("Choose a difficulty level (easy, medium, hard): ")
    secret_word = hangman.difficulty(inputed_difficulty)
    match secret_word:
        case "Error: Invalid difficulty level.":
            print(secret_word)
            is_valid_choice = True
        case _:
            is_valid_choice = False

hangman.hangman(secret_word)