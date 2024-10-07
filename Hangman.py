import Hangman_logic


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

    # Call Hangman_logic.game with the selected category
    if category == 1:
        Hangman_logic.game(fruits)
    elif category == 2:
        Hangman_logic.game(animals)
    elif category == 3:
        Hangman_logic.game(colors)
    elif category == 4:
        Hangman_logic.game(vehicles)
    elif category == 5:
        Hangman_logic.game(countries)
    else:
        print("Invalid category!")

    # Ask if the user wants to play again
    repeat = input("Do you want to play again? Y/N: ").strip().lower()
    if repeat != 'y':
        break
print("Thank you for playing!")