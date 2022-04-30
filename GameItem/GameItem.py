import abc

import pygame


class GameItem(metaclass=abc.ABCMeta):
    """
    游戏内物品抽象基类
    """

    @abc.abstractmethod
    def getPygameSurface(self) -> pygame.Surface:
        """
        抽象方法
        返回pygame可显示的对象 Surface
        """
        pass
