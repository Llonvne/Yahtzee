import os.path
from enum import Enum

from moviepy.editor import *
from pygame.event import Event as Event
from pygame.event import post as post

from events import *
from src.tools import disBG


class SpeedboatDice:
    def __init__(self):
        """
        初始化 pygame 设置
        """

        # 设置窗口大小，分辨率
        self.window_size: tuple = (1280, 720)
        self.caption = "快艇骰子"

        # 设置 LOGO
        logo = pygame.image.load(os.path.join('Media', 'Pic', 'LOGO.jpeg'))
        pygame.display.set_icon(logo)

        # 初始化 pygame 模块
        pygame.init()
        pygame.display.set_caption(self.caption)
        self.screen = pygame.display.set_mode(self.window_size)

        # 显示背景
        disBG.disBg(self.screen)

        # 开头视频
        start0Video = VideoFileClip("Media/Video/Start0720.mp4").subclip(0, 3.3)
        startVideo = VideoFileClip("Media/Video/Start720.mp4").subclip(0, 2.4)
        start0Video.preview()
        startVideo.preview()
        startVideo.close()
        start0Video.close()
        # 刷新视频的结束
        disBG.disBg(self.screen)

        # 加载 BGM
        pygame.mixer.init()
        pygame.mixer.music.load(os.path.join('Media', 'Music', 'BGM.mp3'))
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(100000)

        # 向队列中推入游戏开始事件
        post(Event(GAME_START, {'程序控制事件': '游戏开始'}))

    def run(self):
        """
        启动游戏
        :return:
        """

        # 游戏循环
        # 开始游戏阶段
        running = True
        while running:
            # a.rollNotRemaining()
            # a.displayDices(self.screen)
            # pygame.time.wait(300)
            for event in pygame.event.get():
                # 如果按下了退出按钮
                if event.type == pygame.QUIT:
                    running = False
                # if event.type == GAME_START:

            pygame.display.update()
