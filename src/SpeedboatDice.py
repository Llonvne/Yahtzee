import os.path

import pygame.event
from moviepy.editor import *

from src.GameItem.ScoreBoard import Scoreboard
from src.tools import disBG
from src.tools.disChoice import disChoice
from src.userInput import *


class SpeedboatDice:
    def __init__(self, screen: pygame.Surface):

        self.screen = screen
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
                    break
                # 如果接收到游戏开始
                elif event.type == GAME_START:
                    # 清空队列中保留的用户事件
                    ClearAllUserEventsInQueue()
                    # 立刻推入 RoundStart 事件
                    pygame.event.post(pygame.event.Event(RoundStart))
                elif event.type == GAME_END:
                    pass
                elif event.type == RollEvent:
                    r.diceGroup.rollNotRemaining()
                    r.diceGroup.displayDices(self.screen)
                    pygame.time.wait(300)
                    pygame.display.update()
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
                    r.diceGroup.displayDices(self.screen)
                    disChoice(r.diceGroup, scoreBoards[r.userNo], r.userNo, self.screen)
                else:
                    processUserInput(event, r)
                disBG.disBg(self.screen)
                r.diceGroup.displayDices(self.screen)
                disChoice(r.diceGroup, scoreBoards[r.userNo], r.userNo, self.screen)
                pygame.display.update()
