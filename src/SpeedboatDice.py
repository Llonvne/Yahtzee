import pygame.event

from src.GameData import GameData
from src.events.handler.GameControllerEventHandler import GameControllerEventHandler
from src.events.handler.RollEventHandler import RollEventHandler
from src.events.handler.ScreenEventHandler import ScreenController
from src.userInput import *

# Debug
event_debug = True


class SpeedboatDice:
    def __init__(self, screen: pygame.Surface):

        self.screen = screen

        # 向队列中推入游戏开始事件
        StartGameEvent()

        self.fcclock = pygame.time.Clock()

    def run(self):
        """
        启动游戏
        :return:
        """
        # 初始化游戏数据
        data = GameData(self.screen)

        # 初始化游戏控制事件处理
        gameControllerEventHandler = GameControllerEventHandler(data)

        # 初始化骰子事件控制器
        rollEventHandler = RollEventHandler(data)

        # 初始化屏幕控制器
        screenController = ScreenController(data)

        # 游戏循环
        # 开始游戏阶段
        running = True
        while running:
            for event in pygame.event.get():

                """
                通过 event_debug 定义是否显示事件
                """
                if event_debug and event.type >= pygame.USEREVENT:
                    print(event)

                """
                如果事件类型为退出，则立刻执行退出
                """
                if event.type == pygame.QUIT:
                    running = False
                    quit(0)
                # 游戏程序控制事件
                # {event_type:GameControllerEvent}
                elif event.__dict__.get(event_type) == GameControllerEvent:
                    # 调用GameControllerEventHandler处理
                    gameControllerEventHandler.event(event)
                # 投骰子控制事件
                # {event_type:RollControllerEvent}
                elif event.__dict__.get(event_type) == RollControllerEvent:
                    rollEventHandler.event(event)
                elif event.__dict__.get(event_type) == ScreenControlEvent \
                        or event.__dict__.get(event_type) == ScoreUpdateEvent:
                    screenController.event(event)
                elif event.__dict__.get(event_type) == TimeControlEvent:
                    if event.__dict__.get(sub_type) == WaitEvent:
                        pygame.time.wait(event.__dict__.get('ms'))
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
