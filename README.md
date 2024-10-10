# Hangman Game

This is a simple implementation of the classic Hangman game in Python.

## Project Structure

- `Hangman_logic`: The main script containing the game logic.
- `Categories`: The lists of words used in the game.

## How to Play

1. Run the `main.py` script.
2. The game will randomly select a word from the category provided by the user.
3. Guess letters one at a time.
4. You have a limited number of incorrect guesses before the game ends.

## Screenshots
![J (2)](https://github.com/user-attachments/assets/8fc7fbc5-100b-4846-8e7a-548887d5c6ca)
![J (3)](https://github.com/user-attachments/assets/69239278-d438-47c1-954e-e5803957332b)
![J (1)](https://github.com/user-attachments/assets/7f05605d-8943-496a-bf24-55bedf0918a6)






## Requirements

- Python 3.x

## Running the Game

To start the game, run the following command in your terminal:

```sh
py main.py
```

Here is the Hangman Game Project Report formatted in GitHub Markdown:

# Hangman Game Project Report

## Overview

Hangman is a guessing game where one player thinks of a word, and the other player tries to guess the word by suggesting letters. For each letter that is not in the word, the first player draws a part of a hangman's gallows. The game continues until the word is guessed or the gallows is complete and the player who is guessing the word is "hanged."

In this project, we have created a simple implementation of the Hangman game using Python. The game allows the user to choose a category and then play the game by guessing letters. The game continues until the user guesses the word or runs out of chances.

## Game Structure

The Hangman game is designed with three primary components:

### 1. **Categories**
   - The game includes **five distinct categories**:
     1. **Fruits**: Words related to different types of fruits.
     2. **Animals**: Words that represent names of various animals.
     3. **Colors**: A collection of different color names.
     4. **Vehicles**: Words related to different kinds of vehicles.
     5. **Countries**: Names of countries from around the world.
   - **Purpose of Categories**: These categories provide variety to the game, allowing the user to select a theme for the words they will guess.
   - Each category has a **predefined list of words**, making it easier to associate difficulty levels based on the user's choice.
   - **Word Selection**: Once the category is chosen, a word is selected randomly from the associated list for that category.

### 2. **Game Logic**
   - The game logic is housed in a separate module called `Hangman_logic`.
   - **Core Function**:
     - The `game` function is the heart of this module. It controls the flow of the game from start to finish.
     - **Inputs to the Game**: The function takes a list of words from the chosen category and selects one random word for the player to guess.
   - **Word Representation**:
     - The selected word is represented as underscores (`_`), with each underscore corresponding to a letter in the word.
     - Example: For the word "apple," the initial display will be `_ _ _ _ _`.
   - **Tracking Guesses**:
     - The game tracks the letters guessed by the player, displaying them in place of the underscores if they are correct.
     - Incorrect guesses result in the gradual drawing of the hangman's gallows (or other chosen representation of the player's progress toward losing).
   - **Game Over Scenarios**:
     - The game can end in two ways:
       1. **Victory**: When the player guesses all the letters in the word correctly before running out of chances.
       2. **Defeat**: When the player runs out of chances (i.e., the gallows is fully drawn).

### 3. **Main Program**
   - The main program is the user-facing component of the game.
   - **User Interaction**:
     - It presents a menu displaying the five categories (Fruits, Animals, Colors, Vehicles, Countries).
     - It accepts input from the user to choose one of these categories.
   - **Starting the Game**:
     - Once a category is selected, the main program calls the `game` function from the `Hangman_logic` module and passes the appropriate word list to it.
   - **Game Flow Control**:
     - The main program also handles post-game options, asking the player if they would like to play another round or exit the game.

# Gameplay

The flow of the game is structured in a series of steps to enhance the user experience and provide logical progression. Here's an expanded view of the gameplay process:

### 1. **Category Selection**
   - Upon starting the game, the player is greeted with a menu displaying the available categories: Fruits, Animals, Colors, Vehicles, and Countries.
   - **User Input**: The player selects a category by entering the corresponding number (1-5).
   - **Example**: If the player chooses "Fruits," the game will randomly select a word from the list of fruit names.

### 2. **Word Initialization**
   - Once the category is chosen, a random word is selected from that category’s word list.
   - The word is then represented by a series of underscores (`_`), with each underscore representing a letter in the word.
   - **Example**: If the word is "mango," the display will be `_ _ _ _ _`.

### 3. **Prompt to Guess Letters**
   - The player is then prompted to guess a letter in the word.
   - **Valid Input**:
     - The player must input a **single letter**.
     - The input is case-insensitive, so it doesn’t matter whether the player enters uppercase or lowercase letters.
   - **Invalid Input**:
     - If the player inputs a non-letter character or more than one character, they will receive an error message, and it will count as a lost chance.

### 4. **Correct Letter Guesses**
   - If the guessed letter is **present in the word**:
     - The game reveals the letter in all of the correct positions within the word.
     - Example: If the word is "mango" and the player guesses "a," the display will change to `_ a _ _ _`.
   - **Guessing the Same Letter Again**:
     - If the player guesses a letter that they have already guessed correctly, no penalty is applied, but they will be notified that the letter has already been guessed.

### 5. **Incorrect Letter Guesses**
   - If the guessed letter is **not in the word**:
     - The game updates the drawing of the hangman's gallows or another similar representation.
     - **Chances**:
       - The player starts with a predefined number of chances (usually 10).
       - Each incorrect guess reduces the remaining chances by one.
     - **Progress Display**:
       - After each incorrect guess, the game visually updates to show the current progress toward the hangman being fully drawn.
       - Example: After one incorrect guess, the gallows' base might be drawn, and after subsequent guesses, parts of the hangman (head, torso, limbs) will appear.

### 6. **Game Continuation**
   - The game continues in this loop, alternating between prompting the player for a guess, updating the display, and adjusting the number of remaining chances based on whether the guesses are correct or incorrect.
   - **Feedback to the Player**:
     - After every guess, the player sees:
       - The updated word (with correctly guessed letters revealed).
       - The number of remaining chances.
       - A list of letters they have already guessed.

### 7. **Winning the Game**
   - **Victory Condition**:
     - The player wins the game if they guess all the letters in the word correctly **before running out of chances**.
   - **Victory Message**:
     - Upon winning, the game congratulates the player and displays a success message.
     - Example: "Congratulations! You guessed the word 'mango' correctly!"

### 8. **Losing the Game**
   - **Defeat Condition**:
     - The player loses the game if they fail to guess the word correctly and use up all their chances (i.e., the hangman's gallows is fully drawn).
   - **Defeat Message**:
     - If the player loses, the game displays a message informing them of their loss and reveals the correct word.
     - Example: "You ran out of chances! The correct word was 'mango'."

### 9. **Replay Option**
   - After the game ends (either by victory or defeat), the player is given the option to play another round.
   - **User Choice**:
     - If the player chooses to play again, they are brought back to the category selection menu to start a new game.
     - If the player chooses not to play again, the game ends with a goodbye message.
   - **Looping Mechanism**:
     - This replay feature allows the game to continue as long as the player wants to keep playing.


## Functions and Modules

Here's a brief explanation of the functions and modules used in the game:

- `get_fruits`, `get_animals`, `get_colors`, `get_vehicles`, and `get_countries`: These functions return lists of words for each category.
- `game`: This function takes a list of words as input and plays the game with the user. It selects a random word from the list, displays the word as a series of underscores, and prompts the user to guess letters.
- `Hangman_logic`: This module contains the `game` function.
- `Categories`: This module contains the functions for getting the lists of words for each category.

## Code Explanation

Here's a detailed explanation of the code:

```python
# Import the necessary modules
import Hangman_logic
import Categories

# Display the game menu
print("\033[1;37mWelcome to Hangman!\033[0m")
print("\n\033[3;31mRules: \033[0m")
print('''\033[0;31m
   1. You have to guess the word by entering one letter at a time.
   2. You have 10 chances to guess the word.
   3. If you guess the word before running out of chances, you win!
   4. If you run out of chances, you lose!
      \033[0m''')
print("\033[3;37mCategories: \033[0m")
print()
print("   1. \033[0;33mFruits\033[0m")
print("   2. \033[0;31mAnimals\033[0m")
print("   3. \033[0;34mColors\033[0m")
print("   4. \033[0;35mVehicles\033[0m")
print("   5. \033[0;32mCountries\033[0m")
print()

# Get the user's input and start the game
while True:
    category = int(input("\n\033[0;37mEnter the category number: \033[0m"))
    print()
    if category == 1:
        print("You have selected \033[0;33mFruits!\033[0m")
        Hangman_logic.game(Categories.get_fruits())
    elif category == 2:
        print("You have selected \033[0;31mAnimals\033[0m")
        Hangman_logic.game(Categories.get_animals())
    elif category == 3:
        print("You have selected \033[0;34mColors\033[0m")
        Hangman_logic.game(Categories.get_colors())
    elif category == 4:
        print(" You have selected \033[0;35mVehicles\033[0m")
        Hangman_logic.game(Categories.get_vehicles())
    elif category == 5:
        print("You have selected \033[0;32mCountries\033[0m")
        Hangman_logic.game(Categories.get_countries())
    else:
        print("\033[1;31mInvalid category!!/033[0m")

    # Ask the user if they want to play again
    repeat = input("\nDo you want to play again? Y/N: ").lower()
    if repeat != 'y':
        break
print("Thank you for playing!")
```

The code above displays the game menu, gets the user's input, and starts the game. It uses the `Hangman_logic` module to play the game and the `Categories` module to get the lists of words for each category.

### Categories Module

```python
# Categories module
def get_fruits():
    return ['apple', 'banana', 'mango', 'kiwi', 'orange', 'grapes', 'strawberry', 
            'watermelon', 'papaya', 'pineapple', 'pear', 'peach', 'plum', 'cherry', 
            'apricot', 'pomegranate', 'fig', 'guava', 'lychee', 'blueberry', 
            'raspberry', 'blackberry', 'cantaloupe', 'honeydew', 'dragonfruit']

def get_animals():
    return ['kangaroo', 'koala', 'panda', 'penguin', 'dolphin', 'whale', 'shark', 
            'octopus', 'squid', 'jellyfish', 'starfish', 'seahorse', 'lobster', 
            'crab', 'shrimp', 'snail', 'slug', 'ant', 'bee', 'butterfly', 'moth', 
            'spider', 'scorpion', 'bat', 'rat', 'mouse', 'squirrel', 'rabbit', 
            'deer', 'moose']

def get_colors():
    return ['cyan', 'magenta', 'lime', 'teal', 'indigo', 'violet', 'gold', 'silver', 
            'bronze', 'maroon', 'navy', 'olive', 'coral', 'peach', 'mint', 'lavender', 
            'turquoise', 'salmon', 'beige', 'ivory']

def get_vehicles():
    return ['car', 'truck', 'motorcycle', 'bicycle', 'scooter', 'bus', 'train', 
            'airplane', 'helicopter', 'boat', 'submarine', 'spaceship', 'tractor', 
            'van', 'ambulance', 'firetruck', 'policecar', 'taxi', 'limousine', 
            'skateboard', 'rollerblades']

def get_countries():
    return ['canada', 'brazil', 'argentina', 'france', 'germany', 'italy', 
            'spain', 'portugal', 'netherlands', 'belgium', 'switzerland', 
            'austria', 'sweden', 'norway', 'denmark', 'finland', 'iceland', 
            'russia', 'china', 'japan', 'southkorea', 'india', 'australia', 
            'newzealand', 'southafrica', 'egypt', 'nigeria', 'kenya', 'mexico', 
            'colombia', 'chile', 'peru']
```

The code above defines the functions for getting the lists of words for each category.

### Hangman Logic Module

```python
# Hangman_logic module
import random

def game(data):
    word = random.choice(data)
    print("\n\033[0;37mGuess the word!\033[0m")

    guessed_letters = []
    chances = len(word)
    flag = 0

    while chances != 0 and flag == 0:
        print(f"\nChances left: \033[1;37m{chances}\033[0m")
        for char in word:
            if char in guessed_letters:
                print(char, end=' ')
            else:
                print('_', end=' ')
        print()

        guess = input("\n\033[0;37mEnter a letter to guess: \033[0m")

        if guess.isalpha() and len(guess) == 1:
            if guess in word:
                guessed_letters.append(guess)

                if all(char in guessed_letters for char in word):
                    print("\n\033[36mYou win!\033[0m")
                    flag = 1
                    print("\033[36mYou have guessed the word correctly!\033[0m")
            else:
                print("\033[31mThat letter is not in the word!\

033[0m")
                chances -= 1
        else:
            print("\033[31mInvalid input. Please enter a single letter.\033[0m")
            chances -= 1

    if chances == 0 and flag == 0:
        print("\n\033[1;31mYou lose!\033[0m")
        print(f"\033[0;37mThe word was:  {word}\033[0m")
```

The code above defines the `game` function, which takes a list of words as input and plays the game with the user. It selects a random word from the list, displays the word as a series of underscores, and prompts the user to guess letters.

## Conclusion

In this project, we have created a simple implementation of the Hangman game using Python. The game allows the user to choose a category and then play the game by guessing letters. The game continues until the user guesses the word or runs out of chances. The project demonstrates the use of Python modules, functions, and conditional statements to create an interactive game.
```

This formatting uses proper headings, code blocks, and lists suitable for GitHub Markdown.
