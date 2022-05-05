import pygame
from pygame.mixer import Sound

from src.game.media.media import Media
from src.game.media.playable import Playable


class Effect(Media, Playable):
    """
    音效类
    实现 Media,Playable 类接口
    提供音效加载，播放操作
    音效类 pause 接口实现为空，pygame 中 mixer 无法暂停
    """

    def __init__(self, path: str):
        """
        音效类初始化函数
        提供音效路径即可
        :param path:
        """

        # 初始化音效对象
        self._effect: Sound
        # 初始化 父类 Media 对象
        super().__init__(path)
        # 是否加载标记
        self.isLoad = False

    def _pygameLoad(self) -> None:
        """
        pygame Sound 对象加载函数
        :return: None
        """

        # 如果没有加载
        if not self.isLoad:
            # 检测 mixer 模块是否初始化，
            if pygame.mixer.get_init() is None:
                # 如果没有就初始化 mixer 模块
                pygame.mixer.init()
            # 如果没有加载，加载该对象
            self._effect = pygame.mixer.Sound(self._path)

    def play(self) -> None:
        """
        Playable 的 play 接口
        提供音效播放
        :return:
        """

        # _pygameLoad 将提供音效被加载，且只被加载一次
        self._pygameLoad()

        # 播放 Sound 对象
        self._effect.play()
        pass

    def pause(self) -> None:
        """
        Playable pause 接口
        由于 pygame.mixer 不提供 pause 接口
        此处实现为空
        :return:
        """
        pass
