import os

import pygame

from src.GameItem.GameItem import GameItem

import random

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
        return DicePics[self.value - 1]

    def roll(self):
        self.value = random.randint(1, 6)
