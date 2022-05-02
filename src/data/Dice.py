import os

import pygame

from src.data.GameItem import GameItem

import random

"""
DicePics
"""
DicePics: list = [pygame.image.load(os.path.join('Media', 'Pic', '1.png')),
                  pygame.image.load(os.path.join('Media', 'Pic', '2.png')),
                  pygame.image.load(os.path.join('Media', 'Pic', '3.png')),
                  pygame.image.load(os.path.join('Media', 'Pic', '4.png')),
                  pygame.image.load(os.path.join('Media', 'Pic', '5.png')),
                  pygame.image.load(os.path.join('Media', 'Pic', '6.png'))]


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
        # 是否保留,默认不保留
        self.remaining = False

    def getPygameSurface(self) -> pygame.Surface:
        """
        获得当前 value 对应的 pygame.Surface
        :return: pygame.Surface
        """
        return DicePics[self.value - 1]

    def roll(self) -> int:
        """
        投骰子 使得 value 在 [1,6] 随机取值
        :return: int
        """
        self.value = random.randint(1, 6)
        return self.value
