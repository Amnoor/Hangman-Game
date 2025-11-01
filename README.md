# **Hangman Game**

This repository contains a simple implementation of the classic Hangman game. The game allows users to play against the computer, selecting from different difficulty levels (easy, medium, hard). The game displays the hangman art as the user makes incorrect guesses.



## **Table Of Contents**

- [Key Points](#key-points)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Installation](#installation)
- [Usage](#usage)
- [Contribution](#contribution)
- [License](#license)
- [Acknowledgements](#acknowledgements)



## Key Points

- Playable via the provided executable release or by running the Python scripts.
- Library modules now include clear docstrings:
  - library/hangman_module.py
    - start(): prints a welcome and brief rules.
    - difficulty(difficulty_level): returns a random word for "easy", "medium", or "hard".
    - hangman(secret_word): runs the game loop for a given secret word.
    - help(): prints a short description of available functions.
  - library/hangman_variables.py
    - easy, medium, hard: word lists by difficulty.
    - hangman_art: ASCII art frames for wrong guesses.
    - help(): prints a short description of the variables.



## **Features**

- Different difficulty levels: easy, medium, and hard.
- Dynamic hangman art updates based on the number of incorrect guesses.
- User-friendly interface that shows the current state of the word, guessed letters, and attempts remaining.
- Clear instructions for playing the game.



## **Getting Started**

### **Installation**

To play the Hangman game, You need to install 3 things:

1. Download the latest `Hangman Game v1.0.0.exe` from the Releases
2. Run the `Hangman Game v1.0.0.exe`



## **Usage**

1. When prompted, enter a difficulty level (easy, medium, hard).
2. The game will select a random word based on your chosen difficulty.
3. Guess letters one by one to try and guess the word.
4. Keep track of attempts remaining and guessed letters.
5. The hangman art will update as you make incorrect guesses.



## **Contribution**

Contributions are welcome! If you find any bugs or have ideas for improvements, feel free to open Issue or submit a Pull Request, but if you are gonna make any changes and submit a Pull Request, you have to follow a specific rule:

1. Please fork the repository and create a branch off `develop` (e.g., `feature/your-feature`) and make your changes.
2. After you’ve made your changes, **add your GitHub username** and link it to your GitHub profile in the [Acknowledgement](#acknowledgement) section (for example: `[YourName](https://github.com/YourName)`).
3. Submit a pull request to the `develop` branch for review.
4. Once `develop` is stable and well-tested, we’ll create a release branch (`release/vx.x.x`), merge into `main`, tag it, and publish.



## **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.



## **Acknowledgements**

Thanks to everyone who has contributed to open-source projects and made this game possible.
  
  ```Achnowledgements
  ```
