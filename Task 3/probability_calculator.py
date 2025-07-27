class ProbabilityCalculator:
    def __init__(self, dice_list):
        self.dice_list = dice_list

    @staticmethod
    def win_prob(dice_a, dice_b):
        wins = 0
        total = 0
        for a in dice_a.faces:
            for b in dice_b.faces:
                if a > b: wins += 1
                total += 1
        return wins / total * 100