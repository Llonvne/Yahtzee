import os.path

import pygame.event
from moviepy.editor import *

from src.GameItem.ScoreBoard import Scoreboard
from src.tools import disBG
from src.tools.disChoice import disChoice
from src.userInput import *


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
        # 初始化 ScoreBoard
        scoreBoards = [Scoreboard() for i in range(2)]

        # 初始化回合
        r = Round(scoreBoards)
        roundCount = 0

        # 游戏循环
        # 开始游戏阶段
        running = True
        while running:
            for event in pygame.event.get():
                print(event)
                # 如果按下了退出按钮
                if event.type == pygame.QUIT:
                    running = False
                # 如果接收到游戏开始
                elif event.type == GAME_START:
                    # 清空队列中保留的用户事件
                    ClearAllUserEventsInQueue()
                    # 立刻推入 RoundStart 事件
                    pygame.event.post(pygame.event.Event(RoundStart))
                elif event.type == GAME_END:
                    pass
                # 接收到保留 第 K 个骰子事件
                elif event.type == RemainK:
                    # 停止接受用户输入
                    BlockUserInput()
                    # 清空队列中保留的用户事件
                    ClearAllUserEventsInQueue()
                    # 调用 Round 处理
                    r.remain(event['remaining'])
                # 接收到保留成功后
                elif event.type == RemainKEnd:
                    # 清空队列中保留的用户事件
                    ClearAllUserEventsInQueue()
                    # 开始处理用户事件
                    AllowUserInput()
                # 接收到投骰子事件
                elif event.type == RollNow:
                    # 停止接受用户输入
                    BlockUserInput()
                    # 清空队列中保留的用户事件
                    ClearAllUserEventsInQueue()
                    # 调用 Round 处理 roll 操作
                    r.roll()
                # 接收到Roll结束事件
                elif event.type == RollEnd:
                    disChoice(r.diceGroup, scoreBoards[r.userNo], r.userNo, self.screen)
                    # 清空队列中保留的用户事件
                    ClearAllUserEventsInQueue()
                    # 开始接受用户输入
                    AllowUserInput()
                # 选择 第 K 个分数
                elif event.type == ChooseK:
                    # 立刻停止用户输入
                    BlockUserInput()
                    # 清除队列中用户事件
                    ClearAllUserEventsInQueue()
                    # 调用 Round 处理用户事件
                    r.choose(event['no'])
                elif event.type == ChooseKEnd:
                    AllowUserInput()
                # 接收到 RoundEnd事件
                elif event.type == RoundEnd:
                    BlockUserInput()
                    ClearAllUserEventsInQueue()
                    if roundCount == 12:
                        pygame.event.post(pygame.event.Event(GAME_END))
                    else:
                        pygame.event.post(pygame.event.Event(RoundStart))
                # 接收到 RoundStart
                elif event.type == RoundStart:
                    AllowUserInput()
                    roundCount += 1
                    r = Round(scoreBoards)
                else:
                    processUserInput(event, r)
            pygame.display.update()
