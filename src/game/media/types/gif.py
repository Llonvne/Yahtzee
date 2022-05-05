import os

import pygame
from pygame import Surface

from src.game.media.display.display import Display
from src.game.media.group.PicGroup import PicGroup
from src.game.media.types.pic import Pic


class GIF(Display):
    """
    GIF 类
    提供 GIF 初始化和自动播放

    使用方法：
    提供所有图片组路径组成的列表来初始化 GIF 对象，播放顺序由列表的先后顺序决定

    播放方式：该类已经实现 Display 接口，直接传递给支持 Display 的显示函数既可以显示
    """

    def __init__(self, picGroup: PicGroup):
        """
        初始化函数，由图片组进行初始化，默认顺序由列表先后顺序决定
        :param paths:
        """

        # 调用 PicGroup 处理图片
        self.picGroup = picGroup
        # 定义 Index 变量指示要显示的图片
        self.index = 0
        # 定义是否重复显示
        self.displayOnce = False

    # @classmethod
    # def ConstructFromPicList(cls,picList:list[Pic]):
    #


    def toDisplayable(self) -> tuple | Surface:
        """
        显示函数，负责自动切换图片
        :return:
        """

        # index 指示显示坐标
        self.index += 1

        # 如果达到 len(picGroup)
        if self.index == len(self.picGroup):

            # 如果只显示一次(displayOnce == True)
            if self.displayOnce:
                # 返回 空元组指示 display 函数不显示
                return ()

            # 不然重置 index 从头开始显示
            self.index = 0

        # 返回图像
        return self.picGroup[self.index].toDisplayable()

    def __copy__(self):
        return GIF_initWithPicGroup(self.picGroup)


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


def GIF_initWithPicGroup(picGroup: PicGroup) -> GIF:
    paths = list[str]()
    for pic in picGroup:
        paths.append(pic.getPath())
    return GIF(paths)
