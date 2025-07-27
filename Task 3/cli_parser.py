class CLIParser:
    @staticmethod
    def parse_dice_args(dice_args):
        dice_list = []
        for arg in dice_args:
            faces = [int(x) for x in arg.split(',')]
            if len(set(faces)) < 2:
                raise ValueError("Each die must have at least 2 distinct values.")
            dice_list.append(faces)
        return dice_list
