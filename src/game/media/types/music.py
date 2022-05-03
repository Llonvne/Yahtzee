import pygame

from src.game.media.media import Media
from src.game.media.playable import Playable


class Music(Media, Playable):
    """
    pygame music 包装对象 \n
    继承 Media,Playable
    """

    def _pygameLoad(self) -> None:
        """
        实现 Media 抽象接口，将文件转换为pygame 格式
        :return:
        """
        pygame.mixer.music.load(self._path)
        pass

    def __init__(self, path: str):
        # 调用 media 类 保存文件路径
        super().__init__(path)
        # 保存播放次数变量
        self.__isPlayOnce = False

    def play(self, times: int = 1) -> None:
        """
        实现 playable 接口 播放接口
        :param times:
        :return: None
        """
        # 如果已经播放过
        if not self.__isPlayOnce:
            self._pygameLoad()
            self.__isPlayOnce = True
        # 开始播放
        pygame.mixer.music.play(times)
        # todo 设置播放结束事件
        # pygame.music.set_endevent(
        #
        # )

    def pause(self) -> None:
        """
        实现 playable 暂停接口
        :return:
        """
        # 如果没有初始化，不做任何事
        if self.__isPlayOnce:
            pygame.music.pause()
