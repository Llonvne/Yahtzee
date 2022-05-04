from src.board.Board import Board
from src.dices.diceGroup import DiceGroup


class Player:

    def __init__(self, no):
        self.diceBoard = DiceGroup()
        self.board = Board()
        self.isYourTerm = False
        self.no = no
        self.chance = 2

    def roll(self):
        self.chance -= 1
        self.diceBoard.roll()

    def rollNotCostChances(self):
        self.diceBoard.roll()

    def chooseScore(self, scoreName: str) -> None:
        pass

    def resetInTerm(self):
        self.diceBoard.reset()
        self.chance = 2

    def isHasChance(self):
        return self.chance > 0

    def setRemaining(self, no: int, isRemain: bool):
        self.diceBoard.setRemaining(no, isRemain)

    def isRemain(self, no: int):
        return self.diceBoard.isRemaining(no)
