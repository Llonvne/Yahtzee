import pygame

from src.game.media.display.display import Display
from src.game.media.media import Media


class Pic(Media, Display):
    """
    pygame 图片包装类，采用懒加载
    """

    def __init__(self, path: str):
        super().__init__(path)
        self._pic = None

    def _pygameLoad(self) -> None:
        self._pic = pygame.image.load(self._path)
        pass

    def toDisplayable(self):
        if self._pic is None:
            self._pygameLoad()
        return self._pic

    def __deepcopy__(self):
        return Pic(self._path)
