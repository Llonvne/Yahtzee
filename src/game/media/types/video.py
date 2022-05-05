from moviepy.editor import *

from src.game.media.media import Media
from src.game.media.playable import Playable


class Video(Media, Playable):
    """
    Pygame，MoviePy Video 包装类\n
    继承 Media 和 Playable 类
    """

    def __init__(self, path: str):
        # 调用 Media 类保存路径
        super().__init__(path)
        # 标记变量 _Video 采用懒加载
        self._video = None
        # 保存是否加载
        self.isLoad = False

    def _pygameLoad(self) -> VideoFileClip:
        """
        实现 media 抽象类 转换为pygame格式接口
        :return:
        """
        return VideoFileClip(self._path).subclip()

    def play(self) -> None:
        """
        playable 播放接口
        :return:
        """
        # 如果没有加载，就加载，否则就播放
        if not self.isLoad:
            self._video = self._pygameLoad()
        self._video.preview()

    def pause(self) -> None:
        """
        playable 暂停接口
        :return:
        """
        self._video.pause()
        pass
