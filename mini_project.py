import random

def main_logic(data):
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

print("Welcome to the game!")
# Print the rules of the game
print("Rules:")
print('''
      You have to guess the word.
      You have to guess the word before the chances run out.
      You can only guess one letter at a time.
      You can only guess a letter once.
      ''')

# Lists of words for different categories
fruits = ['apple', 'banana', 'mango', 'kiwi', 'orange', 'grapes', 'strawberry', 
        'watermelon', 'papaya', 'pineapple', 'pear', 'peach', 'plum', 'cherry', 
        'apricot', 'pomegranate', 'fig', 'guava', 'lychee', 'blueberry', 
        'raspberry', 'blackberry', 'cantaloupe', 'honeydew', 'dragonfruit']
animals = ['kangaroo', 'koala', 'panda', 'penguin', 'dolphin', 'whale', 'shark', 
        'octopus', 'squid', 'jellyfish', 'starfish', 'seahorse', 'lobster', 
        'crab', 'shrimp', 'snail', 'slug', 'ant', 'bee', 'butterfly', 'moth', 
        'spider', 'scorpion', 'bat', 'rat', 'mouse', 'squirrel', 'rabbit', 
        'deer', 'moose']
colors = ['cyan', 'magenta', 'lime', 'teal', 'indigo', 'violet', 'gold', 'silver', 
        'bronze', 'maroon', 'navy', 'olive', 'coral', 'peach', 'mint', 'lavender', 
        'turquoise', 'salmon', 'beige', 'ivory''cyan', 'magenta', 'lime', 'teal', 'indigo', 'violet', 'gold', 'silver', 
        'bronze', 'maroon', 'navy', 'olive', 'coral', 'peach', 'mint', 'lavender', 
        'turquoise', 'salmon', 'beige', 'ivory']
vehicles = ['car', 'truck', 'motorcycle', 'bicycle', 'scooter', 'bus', 'train', 
        'airplane', 'helicopter', 'boat', 'submarine', 'spaceship', 'tractor', 
        'van', 'ambulance', 'firetruck', 'policecar', 'taxi', 'limousine', 
        'skateboard', 'rollerblades']

countries = ['canada', 'brazil', 'argentina', 'france', 'germany', 'italy', 
        'spain', 'portugal', 'netherlands', 'belgium', 'switzerland', 
        'austria', 'sweden', 'norway', 'denmark', 'finland', 'iceland', 
        'russia', 'china', 'japan', 'southkorea', 'india', 'australia', 
        'newzealand', 'southafrica', 'egypt', 'nigeria', 'kenya', 'mexico', 
        'colombia', 'chile', 'peru']

# Display category options
print('''
      1. Fruits
      2. Animals
      3. Colors
      4. Vehicles
      5. Countries
      ''')

while True:
    # Get the category choice from the user
    category = int(input("Enter the category number: "))

    # Call main_logic with the selected category
    if category == 1:
        main_logic(fruits)
    elif category == 2:
        main_logic(animals)
    elif category == 3:
        main_logic(colors)
    elif category == 4:
        main_logic(vehicles)
    elif category == 5:
        main_logic(countries)
    else:
        print("Invalid category!")

    # Ask if the user wants to play again
    repeat = input("Do you want to play again? Y/N: ").strip().lower()
    if repeat != 'y':
        break
print("Thank you for playing!")