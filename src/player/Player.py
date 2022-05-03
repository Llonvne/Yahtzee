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
        self.diceBoard.roll()

    def chooseScore(self, scoreName: str) -> None:
        for name, func in self.diceBoard.noTofunc.items():
            if scoreName == name:
                self.board.addScore(name, func)
                return

    def reset(self):
        self.chance = 2
        self.diceBoard.roll()
