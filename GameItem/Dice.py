import pygame

from GameItem.GameItem import GameItem

import random


class Dice(GameItem):
    """
    骰子类型
    """

    def __init__(self):
        """
        骰子初始化方法
        """
        # 初始化骰子值为 0
        self.value = 0

        # todo 加载骰子图片 保存为 Surface
        self.DicePics = []

    def getPygameSurface(self) -> pygame.Surface:
        return self.DicePics[self.value]

    def roll(self):
        self.value = random.randint(1, 6)
