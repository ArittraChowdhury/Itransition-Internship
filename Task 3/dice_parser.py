from dice import Dice

class DiceParser:
    @staticmethod
    def parse(args):
        if len(args) < 3:
            raise ValueError("You must provide at least 3 dice.")

        dice_list = []
        for i, arg in enumerate(args):
            try:
                numbers = [int(x) for x in arg.split(',')]
                if len(numbers) < 1:
                    raise ValueError()
                dice_list.append(Dice(numbers))
            except Exception:
                raise ValueError(f"Invalid format for dice {i+1}: '{arg}'.")
        return dice_list