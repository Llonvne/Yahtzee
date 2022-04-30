import pygame

from GameItem.DiceGroup import DiceGroup
from GameItem.GameItem import GameItem


class Scoreboard(GameItem):
    def getPygameSurface(self) -> pygame.Surface:
        pass

    def __init__(self):
        self.one = 0
        self.two = 0
        self.three = 0
        self.four = 0
        self.five = 0
        self.six = 0

        self.numCount = 0
        self.reward = 0

        self.total = 0
        self.foutSame = 0
        self.calabash = 0
        self.smallStraights = 0
        self.largeStraights = 0
        self.speedboat = 0

    def totalScore(self):
        return self.one + self.two + self.three + self.four + self.five + self.six + \
               self.reward + self.total + self.foutSame + self.calabash + \
               self.smallStraights + self.largeStraights + self.speedboat

    def totalScoreofNumber(self):
        return self.one + self.two + self.three + self.four + self.five + self.six
