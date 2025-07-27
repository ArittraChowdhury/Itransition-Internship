from console_menu import ConsoleMenu
from fair_random_generator import FairRandomGenerator

class FirstMoveDecider:
    def __init__(self, dice_list):
        self.dice_list = dice_list

    def decide(self):
        print("\nLet's decide who goes first.")
        print("Pick 0 or 1:")
        fr = FairRandomGenerator(1)  # range 0–1
        print(f"HMAC: {fr.get_hmac()}")

        user_input = ConsoleMenu.ask_choice(["0", "1", "x", "?"])
        if user_input == "x":
            return None
        elif user_input == "?":
            self.show_help()
            return self.decide()

        try:
            user_number = int(user_input)
        except ValueError:
            print("Invalid input.")
            return self.decide()

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

    def show_help(self):
        print("\nHelp:")
        print("We'll both choose 0 or 1.")
        print("Computer commits first via HMAC, then you choose.")
        print("The sum of both values modulo 2 decides who goes first.")
        print("Result = 1 → You go first.")
        print("Result = 0 → I go first.\n")
