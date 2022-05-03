import pygame

from src.SpeedBoatDice_Beta_2 import config
from src.SpeedBoatDice_Beta_2.game.media.types.music import Music


class Game:
    """
    pygame API 托管类
    这个函数将会包装所有 pygame 接口
    所有对于 pygame 的操作都应该由该类托管
    """

    def __init__(self):
        # 初始化 pygame
        pygame.init()

        # 初始化标题
        pygame.display.set_caption(config.caption)

        # 初始化分辨率，获得显示对象
        self.screen = pygame.display.set_mode(config.window_size)

        # 设置 LOGO
        pygame.display.set_icon(
            pygame.image.load(config.logo)
        )

        # 播放 BGM
        self.BGM = Music(config.default_BGM)
        self.BGM.play()
