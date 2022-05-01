import pygame.event

from src.GameData import GameData
from src.eventHandlers.GameControllerEventHandler import GameControllerEventHandler
from src.eventHandlers.RollEventHandler import RollEventHandler
from src.tools import disBG
from src.userInput import *

# Debug
event_debug = True


class SpeedboatDice:
    def __init__(self, screen: pygame.Surface):

        self.screen = screen

        # 向队列中推入游戏开始事件
        events.StartGameEvent()

    def run(self):
        """
        启动游戏
        :return:
        """
        # 初始化游戏数据
        data = GameData(self.screen)
        # 初始化游戏控制事件处理
        gameControllerEventHandler = GameControllerEventHandler(data, self.screen)
        # 初始化骰子事件控制器
        rollEventHandler = RollEventHandler(data, self.screen)

        # 游戏循环
        # 开始游戏阶段
        running = True
        while running:
            for event in pygame.event.get():

                """
                Event Debug 设置是否显示
                """
                if event_debug:
                    print(event)
                if event.type == pygame.QUIT:
                    running = False
                    break
                    pass

                # --- 游戏程序控制事件 --- # {event_type:GameControllerEvent}
                elif event.__dict__.get(events.event_type) == events.GameControllerEvent:
                    # 调用GameControllerEventHandler处理
                    gameControllerEventHandler.event(event)
                # --- 投骰子控制事件 --- # {event_type:RollControllerEvent}
                elif event.__dict__.get(events.event_type) == events.RollControllerEvent:
                    rollEventHandler.event(event)
                # 选择 第 K 个分数
                elif event.type == ChooseK:
                    # 立刻停止用户输入
                    BlockUserInput()
                    # 清除队列中用户事件
                    ClearAllUserEventsInQueue()
                    # 调用 Round 处理用户事件
                    data.round.choose(event['no'])
                elif event.type == ChooseKEnd:
                    AllowUserInput()
                # 由 processUserInput 处理鼠标的事件
                elif event.type == pygame.MOUSEMOTION:
                    processUserInput(event, data.round)
                disBG.disBg(self.screen)
                data.round.diceGroup.displayDices(self.screen)
                data.displayScore()
                pygame.display.update()
