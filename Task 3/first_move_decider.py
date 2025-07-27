import secrets
from probability_calculator import ProbabilityCalculator
from help_table import HelpTable
from console_menu import ConsoleMenu

class FirstMoveDecider:
    def __init__(self, dice_list):
        self.dice_list = dice_list

    def decide(self):
        print("\nLet's randomly decide who goes first.")
        print("Type '?' to view the help table, or press Enter to continue.")

        while True:
            choice = input("Your input (? or Enter): ").strip().lower()
            if choice == "?":
                self.show_help_table()
            elif choice == "":
                break
            else:
                print("Invalid input. Press Enter to proceed or '?' for help.")

        
        toss = secrets.randbelow(2)

        if toss == 1:
            print("You go first!\n")
            return True
        else:
            print("I go first!\n")
            return False

    def show_help_table(self):
        print("\nShowing probability help table...\n")
        calculator = ProbabilityCalculator(self.dice_list)
        table = HelpTable(calculator)
        table.display()
