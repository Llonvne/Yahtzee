import pygame

from src.GameItem.Dice import Dice


class DiceGroup:
    def displayDices(self, screen: pygame.Surface):
        diff = 550
        for d in self.dice:
            screen.blit(d.getPygameSurface(), (diff, 60))
            diff += 100

    def __init__(self):
        self.dice: list = [Dice() for i in range(5)]

    def setValue(self, no: int, value: int) -> None:
        self.dice[no] = value

    def getValue(self, no: int) -> int:
        return self.dice[no]

    def setRemaining(self, no: int, remaining: bool) -> None:
        self.dice[no].remaining = remaining

    def isRemaining(self, no: int) -> bool:
        return self.dice[no].remaining

    def countK(self, k: int) -> int:
        return sum([k for d in self.dice if d.value == k])

    def total(self) -> int:
        return sum([i.value for i in self.dice])

    def fourSame(self) -> int:
        m = dict()
        for i in self.dice:
            if i.value in m:
                m[i.value] += 1
            else:
                m[i.value] = 1
        for i in m.items():
            if i[1] >= 4:
                return i[0] * 4
        return 0

    def calabash(self) -> int:
        m = dict()
        for i in self.dice:
            if i.value in m:
                m[i.value] += 1
            else:
                m[i.value] = 1
        if len(m) > 2:
            return 0
        m = sorted(m.items(), key=lambda x: x[1])
        if m[0][1] == 2 and m[1][1] == 3:
            return sum([i.value for i in self.dice])
        return 0

    def speedboat(self) -> int:
        if len(set([i.value for i in self.dice])) == 1:
            return 50
        else:
            return 0

    def smallStraights(self):
        if len(set([i.value for i in self.dice])) >= 4:
            return 15
        return 0

    def largeStraights(self):
        if len(set([i.value for i in self.dice])) == 5:
            return 30
        return 0

    def rollNotRemaining(self):
        for d in self.dice:
            if not d.remaining:
                d.roll()
