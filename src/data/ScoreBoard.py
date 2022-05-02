import pygame

from src.data.GameItem import GameItem


class Scoreboard(GameItem):

    def getPygameSurface(self) -> pygame.Surface:
        pass

    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        # 数字区域
        self.one = 0
        self.two = 0
        self.three = 0
        self.four = 0
        self.five = 0
        self.six = 0

        # 奖励分数
        self.reward = 0

        # 组合分数
        self.total = 0
        self.fourSame = 0
        self.calabash = 0
        self.smallStraights = 0
        self.largeStraights = 0
        self.speedboat = 0

    def totalScore(self) -> int:
        """
        计算上述总分
        :return: 总分
        """
        return self.one + self.two + self.three + self.four + self.five + self.six + \
               self.reward + self.total + self.fourSame + self.calabash + \
               self.smallStraights + self.largeStraights + self.speedboat

    def totalScoreofNumber(self) -> int:
        """
        计算数字区域总分
        :return: int
        """
        return self.one + self.two + self.three + self.four + self.five + self.six

    def isReward(self) -> bool:
        return self.totalScoreofNumber() >= 63
