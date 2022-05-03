import os

import pygame

from SpeedboatDice import SpeedboatDice
from src.VideoMusicControl import video, music

if __name__ == '__main__':
    # 初始化 pygame 设置

    # 设置窗口大小，分辨率
    window_size: tuple = (1280, 720)
    caption = "快艇骰子"

    # 设置 LOGO
    logo = pygame.image.load(os.path.join('Media', 'Pic', 'LOGO.jpeg'))
    pygame.display.set_icon(logo)

    # 初始化 pygame 模块
    pygame.init()
    pygame.display.set_caption(caption)
    screen = pygame.display.set_mode(window_size)

    # 播放视频
    video.play()

    # 播放BGM
    music.play()

    # 启动游戏
    SpeedboatDice(screen).run()
