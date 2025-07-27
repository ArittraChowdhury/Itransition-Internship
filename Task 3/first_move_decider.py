from console_menu import ConsoleMenu
from fair_random_generator import FairRandomGenerator
from probability_calculator import ProbabilityCalculator
from help_table import HelpTable

class FirstMoveDecider:
    def __init__(self, dice_list):
        self.dice_list = dice_list

    def decide(self):
        print("\nLet's decide who goes first.")
        print("Pick 0 or 1 (or ? for help table):")
        fr = FairRandomGenerator(1)  # range 0–1
        print(f"HMAC: {fr.get_hmac()}")

        while True:
            user_input = ConsoleMenu.ask_choice(["0", "1", "x", "?"]).strip().lower()

            if user_input == "x":
                return None
            elif user_input == "?":
                self.show_help_table()
                continue

            if user_input not in ("0", "1"):
                print("Invalid input. Please choose 0, 1, ?, or x.")
                continue

            try:
                user_number = int(user_input)
            except ValueError:
                print("Invalid input.")
                continue

            result = fr.get_result(user_number)
            computer_number = result['computer_number']
            key = result['key']
            combined = (user_number + computer_number) % 2

            print(f"Computer chose: {computer_number} (KEY={key})")
            print(f"Combined value: ({user_number} + {computer_number}) % 2 = {combined}")

            if combined == 1:
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
