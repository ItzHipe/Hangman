import random

def game(data):
    word = random.choice(data)
    print("Guess the word!")

    guessed_letters = []
    chances = len(word) + 3
    flag = 0

    while chances != 0 and flag == 0:
        print(f"\nChances left: {chances}")
        for char in word:
            if char in guessed_letters:
                print(char, end=' ')
            else:
                print('_', end=' ')
        print()

        guess = input("\nEnter a letter to guess: ")

        if guess.isalpha() and len(guess) == 1:
            if guess in word:
                guessed_letters.append(guess)

                if all(char in guessed_letters for char in word):
                    print("\nYou win!")
                    flag = 1
                    print("You have guessed the word correctly!")
                    chances += 1
            else:
                print("Boo hoo! That letter is not in the word.")
                chances -= 1
        else:
            print("Invalid input. Please enter a single letter.")
            chances -= 1

    if chances == 0 and flag == 0:
        print("\nYou lose!")
        print("The word was: ", word)
