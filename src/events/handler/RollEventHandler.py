from src.VideoMusicControl import music
from src.data.GameData import GameData
from src.events.events import *
from src.events.handler.EventHandler import EventHandler


class RollEventHandler(EventHandler):
    def __init__(self, data: GameData):

        super().__init__(data)

    def event(self, event: pygame.event.Event):
        if self.get_sub_type(event) == Roll:
            if event.__dict__['times'] > 0:
                # 接收到 Roll 事件后开始 Roll 操作
                self.data.round.diceGroup.rollNotRemaining()
                # 显示背景事件
                displayBackgroundEvent()
                # 显示骰子
                displayDicesEvent()
                # 显示信息
                displayInfoEvent()
                # 执行屏幕更新事件
                screenRefreshEvent()
                # 指定等待事件
                wait(300)
                # 推入下一个事件
                RollEvent(event.__dict__['times'] - 1)
            else:
                RollEndEvent()

        # 接收到保留 第 K 个骰子事件
        elif self.get_sub_type(event) == RemainEvent:
            # 调用 Round 处理
            self.data.round.remain(event['remaining'])

        # 接收到保留成功后
        elif event.type == RemainKEnd:
            pass

        elif self.get_sub_type(event) == Roll_Start:
            # 调用 Round 处理 roll 操作
            self.data.round.roll()

        # 接收到Roll结束事件
        elif self.get_sub_type(event) == Roll_End:
            chooseKEvent(0)
            pass
