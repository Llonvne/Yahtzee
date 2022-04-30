from GameItem.Dice import Dice


class DiceGroup:
    def __init__(self):
        self.dice: list = [Dice() for i in range(5)]

    def countK(self, k: int) -> int:
        return sum([k for d in self.dice if d.value == k])
