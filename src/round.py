from src.GameItem.DiceGroup import DiceGroup


class Round:
    def __init__(self):
        # 初始化 DiceGroup
        diceGroup = DiceGroup()
        # 一共有三次机会
        self.remaining = 3

    def isRemaing(self) -> bool:
        return False

    def isChooseable(self,k:int) -> bool:
        return False
