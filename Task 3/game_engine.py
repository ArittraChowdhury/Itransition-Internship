from first_move_decider import FirstMoveDecider
from console_menu import ConsoleMenu
from fair_random_generator import FairRandomGenerator

class GameEngine:
    def __init__(self, dice_list):
        self.dice_list = dice_list

    def run(self):
        user_first = FirstMoveDecider(self.dice_list).decide()
        if user_first is None:
            return

        if user_first:
            user_die = ConsoleMenu.choose_die(self.dice_list)
            comp_die = next(d for d in self.dice_list if d != user_die)
        else:
            import random
            comp_die = random.choice(self.dice_list)
            print(f"I choose the {comp_die.faces} dice.")
            user_die = ConsoleMenu.choose_die([d for d in self.dice_list if d != comp_die])

        comp_result = self.roll_dice(comp_die, is_user=False)
        print(f"My roll result is {comp_result}")

        user_result = self.roll_dice(user_die, is_user=True)
        print(f"Your roll result is {user_result}")

        if user_result > comp_result:
            print("You win!")
        elif user_result < comp_result:
            print("I win!")
        else:
            print("It's a tie!")

    def roll_dice(self, die, is_user):
        fr = FairRandomGenerator(len(die.faces) - 1)
        print(f"HMAC: {fr.get_hmac()}")

        # Only ask for input if it's the user’s turn
        if is_user:
            face_choices = [str(face) for face in die.faces]

            while True:
                print(f"Choose a number from your die: {', '.join(face_choices)}")
                choice = input("Your selection (or 'x' to exit, '?' for help): ").strip().lower()

                if choice == 'x':
                    exit(0)
                elif choice == '?':
                    ConsoleMenu.show_help_table()
                    continue
                elif choice in face_choices:
                    user_input_index = die.faces.index(int(choice))
                    break
                else:
                    print("Invalid choice. Try again.")
        else:
            import random
            user_input_index = random.randint(0, len(die.faces) - 1)

        result = fr.get_result(user_input_index)
        print(f"Computer's number: {result['computer_number']} (KEY={result['key']})")

        final_index = result['modular_result']
        return die.faces[final_index]
