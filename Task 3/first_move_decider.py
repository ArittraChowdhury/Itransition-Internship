from fair_random_generator import FairRandomGenerator
from console_menu import ConsoleMenu
from probability_calculator import ProbabilityCalculator
from help_table import HelpTable

class FirstMoveDecider:
    def __init__(self, dice_list):
        self.dice_list = dice_list

    def decide(self):
        fr = FairRandomGenerator(1)
        print(f"HMAC: {fr.get_hmac()}")

        while True:
            choice = ConsoleMenu.ask_choice(["0", "1", "X", "?"])
            if choice.lower() == "x":
                return None
            elif choice == "?":
                calc = ProbabilityCalculator(self.dice_list)
                table = HelpTable(calc)
                table.display()
                    
                continue
            elif choice in ("0", "1"):
                result = fr.get_result(int(choice))
                user_first = (int(choice) == result["computer_number"])
                return user_first
            else:
                print("Invalid input. Please enter 0, 1, X or ?")
