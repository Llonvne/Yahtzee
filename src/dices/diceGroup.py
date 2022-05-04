from src.dices.dice import Dice
from src.resetable.resetable import Resetable


class DiceGroup(Resetable):
    def reset(self):
        for dice in self.dices:
            dice.roll()

    def toDisplayable(self):
        display = []
        height = 60
        Left = 550
        diff = 100
        for d in self.dices:
            display.append((d, (Left, height)))
            Left += diff
        return display

    def __init__(self):
        self.dices = [Dice() for i in range(5)]

    def setRemaining(self, no: int, isRemain: bool) -> None:
        """
        Set the remaining of the dice.
        :param no: 骰子的编号
        :param remaining: 是否保留
        :return: None
        """
        self.dices[no].isRemain = isRemain

    def isRemaining(self, no: int) -> bool:
        """
        Check if the dice is remaining.
        :param no: 骰子的编号
        :return: 是否保留
        """
        return self.dices[no].isRemain

    def countK(self, k: int) -> int:
        """
        Count the number of k in DiceGroup.
        :param k: 要求骰子的数值
        :return: 等于k的骰子的数值和
        """
        return sum([k for d in self.dices if d.value == k])

    def total(self) -> int:
        """
        Calculate the total value of the dice group.
        :return: total value
        """
        return sum([i.value for i in self.dices])

    def fourSame(self) -> int:
        """
        Check if the dice group has four same.
        :return: 如果有四个一样，就返回四个一样的数值和，否则返回 0
        """
        m = dict()
        for i in self.dices:
            if i.value in m:
                m[i.value] += 1
            else:
                m[i.value] = 1
        for i in m.items():
            if i[0] == 4:
                return i[0] * 4
        return 0

    def calabash(self) -> int:
        """
        判断是否有葫芦，有则返回所有骰子的数值和，否则返回0
        :return: int
        """
        m = dict()
        for i in self.dices:
            if i.value in m:
                m[i.value] += 1
            else:
                m[i.value] = 1
        if len(m) > 2:
            return 0
        m = sorted(m.items(), key=lambda x: x[1])
        if m[0][1] == 2 and m[1][1] == 3:
            return sum([i.value for i in self.dices])
        return 0

    def speedboat(self) -> int:
        """
        判断是否有飞机，有则返回 50，否则返回0
        :return: int
        """
        if len(set([i.value for i in self.dices])) == 1:
            return 50
        else:
            return 0

    def smallStraights(self):
        """
        判断是否有小顺，有则返回 15，否则返回0
        :return: int
        """
        if len(set([i.value for i in self.dices])) >= 4:
            return 15
        return 0

    def largeStraights(self):
        """
        判断是否有大顺，有则返回 30，否则返回0
        :return: int
        """
        if len(set([i.value for i in self.dices])) == 5:
            return 30
        return 0

    def roll(self) -> None:
        """
        把所有选择不保留的骰子执行 roll 方法
        :return: None
        """
        for d in self.dices:
            d.roll()