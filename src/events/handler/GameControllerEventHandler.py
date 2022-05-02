from src.GameData import GameData
from src.events.handler.EventHandler import EventHandler

from src.events.events import *
from src.round import Round


class GameControllerEventHandler(EventHandler):

    def __init__(self, data: GameData):
        # 构造父类
        super().__init__(data)
        # 局数控制
        self.roundCount = 1

    # 事件处理函数
    def event(self, event: pygame.event.Event):

        # 处理游戏开始事件
        if self.get_sub_type(event) == Game_Start:
            # 推入显示背景事件
            displayBackgroundEvent()
            # 推入屏幕刷新
            screenRefreshEvent()
            # 立刻推入 RoundStart 事件
            RoundStartEvent()

        # 处理游戏结束事件
        elif self.get_sub_type(event) == Game_End:
            pass

        # 处理回合开始事件
        elif self.get_sub_type(event) == Round_Start:
            self.roundCount += 1
            self.data.round = Round(self.data.scoreBoards)
            displayInfoEvent()
            RollStartEvent()

        # 处理回合结束事件
        elif self.get_sub_type(event) == Round_End:
            if self.roundCount == 12:
                EndGameEvent()
            else:
                RoundStartEvent()
