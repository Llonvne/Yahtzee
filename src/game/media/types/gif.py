import os

import pygame

from src.game.media.display.display import Display
from src.game.media.group.PicGroup import PicGroup


class GIF(Display):
    def __init__(self, paths: list[str]):
        self.picGroup = PicGroup(paths)
        self.index = 0

    def toDisplayable(self) -> pygame.Surface:
        self.index += 1
        if self.index == len(self.picGroup):
            self.index = 0
        return self.picGroup[self.index].toDisplayable()


def get_files(filepath: str) -> dict:
    pathToName = dict()
    for filepath, dirnames, filenames in os.walk(filepath):
        for filename in filenames:
            pathToName[os.path.join(filepath, filename)] = filename
    return pathToName


if __name__ == "__main__":
    fcclock = pygame.time.Clock()
    path = list()
    for key in sorted(get_files("Media/GIFTEST").items(), key=lambda x: int(x[1][6:8])):
        path.append(key[0])
    g = GIF(path)
    screen = pygame.display.set_mode((720, 720))
    while True:
        screen.blit(g.toDisplayable(), (0, 0))
        pygame.display.update()
        screen.fill((0, 0, 0))
        fcclock.tick(10)
