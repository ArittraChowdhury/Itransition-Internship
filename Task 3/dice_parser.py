class DiceParser:
    def __init__(self, args):
        self.args = args

    def parse(self):
        from dice import Dice  # Assuming dice.py has the Dice class

        dice_list = []
        for arg in self.args:
            try:
                faces = [int(x) for x in arg.split(",")]
                if len(faces) == 0:
                    raise ValueError("Dice must have at least one face.")
                dice_list.append(Dice(faces))
            except ValueError:
                raise ValueError(f"Invalid dice format: {arg}")
        return dice_list
