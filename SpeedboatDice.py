import os.path

import pygame


class SpeedboatDice:
    def __init__(self):

        # 设置窗口大小，分辨率
        self.window_size: tuple = (1280, 720)
        self.caption = "快艇骰子"

        # 初始化 pygame 模块
        pygame.init()
        pygame.display.set_caption(self.caption)
        self.screen = pygame.display.set_mode(self.window_size)

        # 加载图像,并显示
        self.board = pygame.image.load(os.path.join('Pic', 'board.png'))
        self.screen.blit(self.board, (0, 0))

        # 加载 BGM
        pygame.mixer.init()
        pygame.mixer.music.load(os.path.join('Music', 'BGM.mp3'))
        pygame.mixer.music.play(100000)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                # 如果按下了退出按钮
                if event.type == pygame.QUIT:
                    running = False
            pygame.display.update()
