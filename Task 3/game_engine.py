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
            comp_die = self.dice_list[1]  
            print(f"I choose the {comp_die.faces} dice.")
            user_die = ConsoleMenu.choose_die([d for d in self.dice_list if d != comp_die])

        comp_result = self.roll_dice(comp_die)
        print(f"My roll result is {comp_result}")

        user_result = self.roll_dice(user_die)
        print(f"Your roll result is {user_result}")

        if user_result > comp_result:
            print("You win!")
        elif user_result < comp_result:
            print("I win!")
        else:
            print("It's a tie!")

    def roll_dice(self, die):
        fr = FairRandomGenerator(len(die.faces) - 1)
        print(f"HMAC: {fr.get_hmac()}")
        user_input = int(ConsoleMenu.ask_choice([str(i) for i in range(len(die.faces))]))
        result = fr.get_result(user_input)
        print(f"Computer's number: {result['computer_number']} (KEY={result['key']})")
        final_index = result['modular_result']
        return die.faces[final_index]