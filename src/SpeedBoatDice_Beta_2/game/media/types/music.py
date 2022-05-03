import pygame.music

from src.SpeedBoatDice_Beta_2.game.media.media import Media
from src.SpeedBoatDice_Beta_2.game.media.playable import Playable


class Music(Media, Playable):
    """
    pygame music 包装对象
    继承 Media,Playable
    """

    def __pygameLoad(self) -> None:
        return pygame.music.load(self._path)
        pass

    def __init__(self, path: str):
        # 调用 media 类 保存文件路径
        super().__init__(path)
        # 保存播放次数变量
        self.__isPlayOnce = False

    def play(self, times: int = 1):
        # 如果已经播放过
        if not self.__isPlayOnce:
            self.__pygameLoad()
            self.__isPlayOnce = True
        # 开始播放
        pygame.music.play(times)
        # todo 设置播放结束事件
        # pygame.music.set_endevent(
        #
        # )

    def pause(self):
        # 如果没有初始化，不做任何事
        if self.__isPlayOnce:
            pygame.music.pause()
