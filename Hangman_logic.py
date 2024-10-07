import random

def game(data):
    # Select a random word from the provided data list
    word = random.choice(data)
    print("Guess the word!")

    guessed_letters = []  # List to store guessed letters
    chances = len(word) + 3  # Number of chances given to the player
    flag = 0  # Flag to indicate if the word has been guessed

    while chances != 0 and flag == 0:
        print(f"\nChances left: {chances}")
        chances -= 1

        # Display the word with guessed letters and underscores for remaining letters
        for char in word:
            if char in guessed_letters:
                print(char, end=' ')
            else:
                print('_', end=' ')
        print()

        guess = input("\nEnter a letter to guess: ")

        # Check if the input is a single alphabet letter
        if guess.isalpha() and len(guess) == 1:
            if guess in word:
                guessed_letters.append(guess)

                # Check if all letters in the word have been guessed
                if all(char in guessed_letters for char in word):
                    print("\nYou win!")
                    flag = 1
                    print("You have guessed the word correctly!")
            elif len(guess.split()) > 1 or not guess.isalpha():
                print("Enter only a letter!")
        else:
            print("Enter only a letter!")

    if chances == 0:
        print("\nYou lose!")
        print("The word was: ", word)