import os

import pygame

from src.GameItem.GameItem import GameItem

import random

DicePics: list = [pygame.image.load(os.path.join('Pic', 'one.png')),
                  pygame.image.load(os.path.join('Pic', 'three.png'))
                  ]


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
        return DicePics[self.value]

    def roll(self):
        self.value = random.randint(1, 6)
