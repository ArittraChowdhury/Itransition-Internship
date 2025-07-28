import sys
from dice_parser import DiceParser
from game_engine import GameEngine

if __name__ == "__main__":
    args = sys.argv[1:]  
    if len(args) < 3:
        print("Error: You must provide at least 3 dice as command-line arguments.")
        print("Example: python main.py \"1,2,3,4,5,6\" \"6,6,6,6,6,6\" \"2,2,2,2,3,3\"")
        sys.exit(1)

    try:
        dice_list = DiceParser(args).parse()
    except ValueError as e:
        print("Error parsing dice:", e)
        sys.exit(1)

    GameEngine(dice_list).run()
