import abc

import pygame


class Display(metaclass=abc.ABCMeta):
    """
    Display Object
    可显示对象基本类型
    子类必须实现 toDisplayable 来显示
    """

    @abc.abstractmethod
    def toDisplayable(self) -> pygame.Surface | tuple:
        """
        转化为 pygame.Surface 对象用于显示
        同时可以返回 元组（为空，不为空也不与处理) 来不显示任何事物
        :return: pygame.Surface | Tuple
        """
        pass
