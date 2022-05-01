import os

import pygame

from src.GameItem.GameItem import GameItem

import random

"""
DicePics
"""
DicePics: list = [pygame.image.load(os.path.join('Media', 'Pic', 'one.png')),
                  pygame.image.load(os.path.join('Media', 'Pic', 'two.png')),
                  pygame.image.load(os.path.join('Media', 'Pic', 'three.png')),
                  pygame.image.load(os.path.join('Media', 'Pic', 'four.png')),
                  pygame.image.load(os.path.join('Media', 'Pic', 'five.png')),
                  pygame.image.load(os.path.join('Media', 'Pic', 'six.png'))]


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
