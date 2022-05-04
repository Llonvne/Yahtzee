import pygame
from pygame.mixer import Sound

from src.game.media.media import Media
from src.game.media.playable import Playable


class Effect(Media, Playable):

    def __init__(self, path: str):
        self._effect: Sound
        super().__init__(path)
        self.isLoad = False

    def _pygameLoad(self):
        if not self.isLoad:
            if pygame.mixer.get_init() is None:
                pygame.mixer.init()
            self._effect = pygame.mixer.Sound(self._path)

    def play(self) -> None:
        self._pygameLoad()
        self._effect.play()
        pass

    def pause(self) -> None:
        """
        音效不提供 pause 实现
        :return:
        """
        pass
