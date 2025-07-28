class DiceParser:
    def __init__(self, args):
        self.args = args

    def parse(self):
        from dice import Dice  

        dice_list = []
        for arg in self.args:
            try:
                faces = [int(x) for x in arg.split(",")]
                if len(faces) != 6:
                    raise ValueError("Each die must have exactly 6 faces.")
                dice_list.append(Dice(faces))
            except ValueError:
                raise ValueError(f"Invalid dice format: {arg}")
        return dice_list
