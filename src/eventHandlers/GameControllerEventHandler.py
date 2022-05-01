from src import userInput, events
from src.GameData import GameData
from src.eventHandlers.EventHandler import EventHandler

from src.events import *
from src.round import Round
from src.userInput import ClearAllUserEventsInQueue, BlockUserInput


class GameControllerEventHandler(EventHandler):

    def __init__(self, data: GameData, screen: pygame.Surface):
        # 构造父类
        super().__init__(data)
        # 局数控制
        self.roundCount = 1
        # screen
        self.screen = screen

    # 事件处理函数
    def event(self, event: pygame.event.Event):

        # 处理游戏开始事件
        if self.get_sub_type(event) == Game_Start:
            # 清空队列中保留的用户事件
            ClearAllUserEventsInQueue()
            # 立刻推入 RoundStart 事件
            events.RoundStartEvent()

        # 处理游戏结束事件
        elif self.get_sub_type(event) == events.Game_End:
            pass

        # 处理回合开始事件
        elif self.get_sub_type(event) == Round_Start:
            userInput.AllowUserInput()
            self.roundCount += 1
            self.data.round = Round(self.data.scoreBoards)
            self.data.round.diceGroup.displayDices(self.screen)
            self.data.displayScore()

        # 处理回合结束事件
        elif self.get_sub_type(event) == events.Round_End:
            BlockUserInput()
            ClearAllUserEventsInQueue()
            if self.roundCount == 12:
                EndGameEvent()
            else:
                RoundStartEvent()
