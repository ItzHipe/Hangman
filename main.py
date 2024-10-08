import Hangman_logic
import Categories

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
print("   3. \033[0;30mColors\033[0m")
print("   4. \033[0;35mVehicles\033[0m")
print("   5. \033[0;32mCountries\033[0m")
print()

while True:
    category = int(input("Enter the category number: "))
    print()
    if category == 1:
      print("You have selected \033[0;33mFruits!\033[0m")
      Hangman_logic.game(Categories.get_fruits())
    elif category == 2:
      print("You have selected \033[0;31mAnimals\033[0m")
      Hangman_logic.game(Categories.get_animals())
    elif category == 3:
      print("You have selected \033[0;30mColors\033[0m")
      Hangman_logic.game(Categories.get_colors())
    elif category == 4:
      print("You have selected \033[0;35mVehicles\033[0m")
      Hangman_logic.game(Categories.get_vehicles())
    elif category == 5:
      print("You have selected \033[0;32mCountries\033[0m")
      Hangman_logic.game(Categories.get_countries())
    else:
      print("Invalid category!")

    repeat = input("Do you want to play again? Y/N: ").lower()
    if repeat != 'y':
      break
print("Thank you for playing!")