from moviepy.editor import *

from src.SpeedBoatDice_Beta_2.game.media.media import Media
from src.SpeedBoatDice_Beta_2.game.media.playable import Playable


class Video(Media, Playable):
    """
    Pygame，MoviePy Video 包装类
    继承 Media 和 Playable 类
    """

    def __init__(self, path: str):
        # 调用 Media 类保存路径
        super().__init__(path)
        # 保存 Video 变量
        self.video: VideoFileClip

    def __pygameLoad(self) -> None:
        self.video: Video = Video(self._path)

    def play(self):
        self.video.play()

    def pause(self):
        self.video.pause()
        pass
