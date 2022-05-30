from src.dices.dice import Dice
from src.game.media.display.display import Display
from src.resetable.resetable import Resetable


class DiceGroup(Resetable):
    def reset(self) -> None:
        """
        Resetable reset 接口，提供 DiceGroup 重置接口
        :return: None
        """
        for i in self.__dices:
            i.isRemain = False
        self.roll()

    def toDisplayable(self) -> list[tuple[Display, tuple[int, int]]]:
        """
        转换为可显示对象
        :return: list[tuple[Display,tuple[int,int]]]
        """
        display = []
        height = 200
        Left = 550
        diff = 100
        for d in self.__dices:
            display.append((d, (Left, height)))
            Left += diff
        return display

    def __init__(self):
        """
        初始化 5 个骰子
        """
        self.__dices = [Dice() for i in range(5)]

    def setRemaining(self, no: int, isRemain: bool) -> None:
        """
        Set the remaining of the dice.
        :param no: 骰子的编号
        :param remaining: 是否保留
        :return: None
        """
        self.__dices[no].isRemain = isRemain

    def isRemaining(self, no: int) -> bool:
        """
        Check if the dice is remaining.
        :param no: 骰子的编号
        :return: 是否保留
        """
        return self.__dices[no].isRemain

    def countK(self, k: int) -> int:
        """
        Count the number of k in DiceGroup.
        :param k: 要求骰子的数值
        :return: 等于k的骰子的数值和
        """
        return sum([k for d in self.__dices if d.getValue() == k])

    def total(self) -> int:
        """
        Calculate the total value of the dice group.
        :return: total value
        """
        return sum([i.getValue() for i in self.__dices])

    def fourSame(self) -> int:
        """
        Check if the dice group has four same.
        :return: 如果有四个一样，就返回四个一样的数值和，否则返回 0
        """
        m = dict()
        for i in self.__dices:
            if i.getValue() in m:
                m[i.getValue()] += 1
            else:
                m[i.getValue()] = 1
        v = sorted(m.items(),key=lambda x:x[1],reverse=True)
        print(v)
        if v[0][1] == 4:
            return v[0][0] * 4
        return 0

    def calabash(self) -> int:
        """
        判断是否有葫芦，有则返回所有骰子的数值和，否则返回0
        :return: int
        """
        m = dict()
        for i in self.__dices:
            if i.getValue() in m:
                m[i.getValue()] += 1
            else:
                m[i.getValue()] = 1
        if len(m) > 2:
            return 0
        m = sorted(m.items(), key=lambda x: x[1])
        if m[0][1] == 2 and m[1][1] == 3:
            return sum([i.getValue() for i in self.__dices])
        return 0

    def speedboat(self) -> int:
        """
        判断是否有飞机，有则返回 50，否则返回0
        :return: int
        """
        if len(set([i.getValue() for i in self.__dices])) == 1:
            return 50
        else:
            return 0

    def smallStraights(self):
        """
        判断是否有小顺，有则返回 15，否则返回0
        :return: int
        """
        s = set([i.getValue() for i in self.__dices])
        if len(s) < 4:
            return 0
        if (1 in s and 2 in s and 3 in s and 4 in s) or (5 in s and 2 in s and 3 in s and 4 in s)\
                or (5 in s and 6 in s and 3 in s and 4 in s):
            return 15
        return 0

    def largeStraights(self):
        """
        判断是否有大顺，有则返回 30，否则返回0
        :return: int
        """
        if len(set([i.getValue() for i in self.__dices])) == 5:
            return 30
        return 0

    def roll(self) -> None:
        """
        把所有选择不保留的骰子执行 roll 方法
        :return: None
        """
        for d in self.__dices:
            d.roll()
