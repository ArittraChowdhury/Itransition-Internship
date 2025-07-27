from dice_parser import DiceParser
from game_engine import GameEngine
import sys

args = []
try:
    num_dice = int(input("How many dice do you want to input? (min 3): ").strip())
    if num_dice < 3:
        raise ValueError("You must provide at least 3 dice.")
    for i in range(num_dice):
        die_input = input(f"Enter die {i + 1} (comma-separated numbers): ")
        args.append(die_input.strip())
except ValueError as e:
    print("Error:", e)
    print("Usage: Enter number of dice >= 3. Each die like: 2,2,4,4,9,9")
    sys.exit(1)

# ✅ Parse the dice input strings into Dice objects
try:
    dice_list = DiceParser(args).parse()
except ValueError as e:
    print("Error parsing dice:", e)
    sys.exit(1)

# ✅ Run the game
GameEngine(dice_list).run()
