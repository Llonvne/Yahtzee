import pygame.event

from src import events
from src.GameItem import ScoreBoard
from src.GameItem.DiceGroup import DiceGroup


class Round:
    def __init__(self, scoreBoard: list[ScoreBoard]):
        # 初始化 DiceGroup
        self.diceGroup = DiceGroup()
        self.diceGroup.rollNotRemaining()
        pygame.event.post(pygame.event.Event(events.RollNow, {"RollNow": "1"}))
        # 一共有三次机会
        self.chance1 = 3
        self.chance2 = 3
        # 从第一个开始
        self.userNo = 0
        # 保留记分板引用
        self.scoreBoard = scoreBoard

    def isRemaing(self, k: int) -> bool:
        return self.diceGroup.isRemaining(k)

    def isChooseable(self, k: int) -> bool:
        if k == 0:
            return self.scoreBoard[self.userNo].one < 0
        elif k == 1:
            return self.scoreBoard[self.userNo].two < 0
        elif k == 2:
            return self.scoreBoard[self.userNo].three < 0
        elif k == 3:
            return self.scoreBoard[self.userNo].four < 0
        elif k == 4:
            return self.scoreBoard[self.userNo].five < 0
        elif k == 5:
            return self.scoreBoard[self.userNo].six < 0
        elif k == 6 or k == 7:
            return False
        elif k == 8:
            return self.scoreBoard[self.userNo].total < 0
        elif k == 9:
            return self.scoreBoard[self.userNo].fourSame < 0
        elif k == 10:
            return self.scoreBoard[self.userNo].calabash < 0
        elif k == 11:
            return self.scoreBoard[self.userNo].smallStraights < 0
        elif k == 12:
            return self.scoreBoard[self.userNo].largeStraights < 0
        elif k == 13:
            return self.scoreBoard[self.userNo].speedboat < 0
        else:
            return False

    def remain(self, k: int):
        self.diceGroup.setRemaining(k, not self.diceGroup.isRemaining(k))

    def roll(self):
        if self.userNo == 1:
            if self.chance1 > 0:
                # 引发 RollEvent 事件
                pygame.event.post(pygame.event.Event(events.RollEvent, {"RollEvent": 1}))
                pygame.event.post(pygame.event.Event(events.RollEvent,{"RollEvent": 1}))
                pygame.event.post(pygame.event.Event(events.RollEvent,{"RollEvent": 1}))
                pygame.event.post(pygame.event.Event(events.RollEvent,{"RollEvent": 1}))
                # 引发 RollEnd 事件
                pygame.event.post(pygame.event.Event(events.RollEnd))
                self.chance1 -= 1
        else:
            if self.chance2 > 0:
                # 引发 RollEvent 事件
                pygame.event.post(pygame.event.Event(events.RollEvent,{"RollEvent": 1}))
                pygame.event.post(pygame.event.Event(events.RollEvent,{"RollEvent": 1}))
                pygame.event.post(pygame.event.Event(events.RollEvent,{"RollEvent": 1}))
                pygame.event.post(pygame.event.Event(events.RollEvent,{"RollEvent": 1}))
                # 引发 RollEnd 事件
                pygame.event.post(pygame.event.Event(events.RollEnd))
                self.chance2 -= 1
        pass

    def choose(self, k: int):
        # 引发 chooseEnd 事件
        pygame.event.post(pygame.event.Event(events.ChooseKEnd))
        if k == 0:
            self.scoreBoard[self.userNo].one += self.diceGroup.countK(1)
        elif k == 1:
            self.scoreBoard[self.userNo].two += self.diceGroup.countK(2)
        elif k == 2:
            self.scoreBoard[self.userNo].one += self.diceGroup.countK(3)
        elif k == 3:
            self.scoreBoard[self.userNo].one += self.diceGroup.countK(4)
        elif k == 4:
            self.scoreBoard[self.userNo].one += self.diceGroup.countK(5)
        elif k == 5:
            self.scoreBoard[self.userNo].one += self.diceGroup.countK(6)
        elif k == 8:
            self.scoreBoard[self.userNo].total += self.diceGroup.total()
        elif k == 9:
            self.scoreBoard[self.userNo].fourSame += self.diceGroup.fourSame()
        elif k == 10:
            self.scoreBoard[self.userNo].calabash += self.diceGroup.calabash()
        elif k == 11:
            self.scoreBoard[self.userNo].smallStraights += self.diceGroup.smallStraights()
        elif k == 12:
            self.scoreBoard[self.userNo].largeStraights += self.diceGroup.largeStraights()
        elif k == 13:
            self.scoreBoard[self.userNo].speedboat += self.diceGroup.speedboat()
