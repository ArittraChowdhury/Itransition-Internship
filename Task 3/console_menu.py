from help_table import HelpTable
from probability_calculator import ProbabilityCalculator

class ConsoleMenu:
    @staticmethod
    def choose_die(dice_list):
        print("Choose your dice:")
        for idx, die in enumerate(dice_list):
            print(f"{idx} - {', '.join(str(x) for x in die.faces)}")
        while True:
            choice = input("Your selection: ").strip().lower()
            if choice == '?':
                ConsoleMenu.show_help(dice_list)
                continue
            elif choice == 'x':
                print("Exiting the game.")
                exit(0)
            elif choice.isdigit() and int(choice) in range(len(dice_list)):
                return dice_list[int(choice)]
            else:
                print("Invalid choice. Try again.")

    @staticmethod
    def ask_choice(valid_choices):
        while True:
            print("0 - 0\n1 - 1\nX - exit\n? - help")
            selection = input("Your selection: ").strip().upper()
            if selection in valid_choices:
                return selection
            print("Invalid input.")

    @staticmethod
    def show_help(dice_list):
        calc = ProbabilityCalculator(dice_list)
        table = HelpTable(calc)
        table.display()
