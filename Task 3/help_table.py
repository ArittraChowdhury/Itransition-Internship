from tabulate import tabulate
from probability_calculator import ProbabilityCalculator

class HelpTable:
    def __init__(self, calculator):
        self.calculator = calculator

    def display(self):
        dice_list = self.calculator.dice_list
        headers = [""] + [f"Die {i}" for i in range(len(dice_list))]
        rows = []
        for i, d1 in enumerate(dice_list):
            row = [f"Die {i}"]
            for j, d2 in enumerate(dice_list):
                if i == j:
                    row.append("--")
                else:
                    win_prob = self.calculator.win_prob(d1, d2)
                    row.append(f"{win_prob:.1f}%")
            rows.append(row)
        print(tabulate(rows, headers=headers, tablefmt="grid"))