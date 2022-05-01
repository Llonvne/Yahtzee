import pygame

from src import events
from src.GameData import GameData
from src.eventHandlers.EventHandler import EventHandler
from src.userInput import BlockUserInput, ClearAllUserEventsInQueue, AllowUserInput


class RollEventHandler(EventHandler):
    def __init__(self, data: GameData, screen: pygame.Surface):

        super().__init__(data)
        self.screen = screen

    def event(self, event: pygame.event.Event):
        if self.get_sub_type(event) == events.Roll:
            self.data.round.diceGroup.rollNotRemaining()
            self.data.round.diceGroup.displayDices(self.screen)
            pygame.time.wait(300)
            pygame.display.update()

        # 接收到保留 第 K 个骰子事件
        elif self.get_sub_type(event) == events.RemainEvent:
            # 停止接受用户输入
            BlockUserInput()
            # 清空队列中保留的用户事件
            ClearAllUserEventsInQueue()
            # 调用 Round 处理
            self.data.round.remain(event['remaining'])
        # 接收到保留成功后
        elif event.type == events.RemainKEnd:
            # 清空队列中保留的用户事件
            ClearAllUserEventsInQueue()
            # 开始处理用户事件
            AllowUserInput()
            # 接收到投骰子事件
        elif self.get_sub_type(event) == events.Roll_Start:
            # 停止接受用户输入
            BlockUserInput()
            # 清空队列中保留的用户事件
            ClearAllUserEventsInQueue()
            # 调用 Round 处理 roll 操作
            self.data.round.roll()
        # 接收到Roll结束事件
        elif self.get_sub_type(event) == events.Round_End:
            # 清空队列中保留的用户事件
            ClearAllUserEventsInQueue()
            # 开始接受用户输入
            AllowUserInput()
