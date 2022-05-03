import abc

import pygame


class Display(metaclass=abc.ABCMeta):
    """
    Display Object
    可显示对象基本类型
    子类必须实现 toDisplayable 来显示
    """

    @abc.abstractmethod
    def toDisplayable(self) -> pygame.Surface:
        pass
