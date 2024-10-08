import Hangman_logic
import Categories

print('''Welcome to the game!
Rules:

  You have to guess the word.
  You have to guess the word before the chances run out.
  You can only guess one letter at a time.
  You can only guess a letter once.
  
Categories: 

  1. Fruits
  2. Animals
  3. Colors
  4. Vehicles
  5. Countries
''')

while True:
    category = int(input("Enter the category number: "))
    print()
    if category == 1:
      print("You have selected Fruits!")
      Hangman_logic.game(Categories.get_fruits())
    elif category == 2:
      print("You have selected Animals!")
      Hangman_logic.game(Categories.get_animals())
    elif category == 3:
      print("You have selected Colors!")
      Hangman_logic.game(Categories.get_colors())
    elif category == 4:
      print("You have selected Vehicles!")
      Hangman_logic.game(Categories.get_vehicles())
    elif category == 5:
      print("You have selected Countries!")
      Hangman_logic.game(Categories.get_countries())
    else:
      print("Invalid category!")

    repeat = input("Do you want to play again? Y/N: ").lower()
    if repeat != 'y':
      break
print("Thank you for playing!")