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
                    chances += 1
            else:
                print("\033[31mThat letter is not in the word!\033[0m")
                chances -= 1
        else:
            print("\033[31mInvalid input. Please enter a single letter.\033[0m")
            chances -= 1

    if chances == 0 and flag == 0:
        print("\n\033[1;31mYou lose!\033[0m")
        print(f"\033[0;37mThe word was:  {word}\033[0m")