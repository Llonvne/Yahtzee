import os.path
from enum import Enum

import pygame


class SpeedboatDice:
    def __init__(self):
        """
        初始化 pygame 设置
        """

        # 设置窗口大小，分辨率
        self.window_size: tuple = (1280, 720)
        self.caption = "快艇骰子"

        # 初始化 pygame 模块
        pygame.init()
        pygame.display.set_caption(self.caption)
        self.screen = pygame.display.set_mode(self.window_size)

        # 加载图像,并显示
        self.board = pygame.image.load(os.path.join('Media', 'Pic', 'board2.png'))
        self.screen.blit(self.board, (0, 0))

        # 加载 BGM
        pygame.mixer.init()
        pygame.mixer.music.load(os.path.join('Media', 'Music', 'BGM.mp3'))
        pygame.mixer.music.play(100000)

    @staticmethod
    def run():
        """
        启动游戏
        :return:
        """

        class GameStage(Enum):
            """
            游戏阶段枚举类
            """
            START = 0
            ROLL = 1
            ROLL_OVER = 2
            CHOOSE_REMAINING = 3
            SCORE_CHOOSE = 4
            DIS_SCORE = 5

        # 初始化游戏阶段
        stage = GameStage.START

        # 游戏循环
        # 开始游戏阶段
        running = True
        while running:
            for event in pygame.event.get():
                # 如果按下了退出按钮
                if event.type == pygame.QUIT:
                    running = False
                # 如果是 START
                elif stage == GameStage.START:
                    pass
                elif stage == GameStage.ROLL:
                    pass
            pygame.display.update()
