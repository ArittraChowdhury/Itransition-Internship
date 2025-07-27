from dice_parser import DiceParser
from game_engine import GameEngine
import sys


try:
    args = []
    print("Enter 3 custom dice. Each die should be a comma-separated list of numbers (e.g., 1,2,3,4,5,6):")
    for i in range(3):
        die_input = input(f"Enter die {i + 1}: ")
        args.append(die_input.strip())

    dice_list = DiceParser.parse(args)
except ValueError as e:
    print("Error:", e)
    print("Usage: python main.py 2,2,4,4,9,9 6,8,1,1,8,6 7,5,3,7,5,3")
    sys.exit(1)

GameEngine(dice_list).run()
