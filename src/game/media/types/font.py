import pygame

from src.game.media.display.display import Display


class Font(Display):
    """
    Font 类
    该类还未设计完毕

    todo 字体类设计
    """
    def __init__(self, value: str, color: tuple[int, int, int], size: int):
        """
        显示字体初始化函数
        :param value: 显示的值
        :param color: 颜色
        :param size: 大小
        """
        self.value = value
        self.color = color
        self.size = size

        self.Font = None
        self.displayable = None

    def toDisplayable(self) -> pygame.Surface | tuple:
        if self.Font is None:
            self.Font = pygame.font.Font(pygame.font.get_default_font(), self.size)
        if self.displayable is None:
            self.displayable = self.Font.render(self.value, True, self.color, None)
        return self.displayable
