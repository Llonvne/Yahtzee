from random import randint

from src import config
from src.game.media.display.display import Display
from src.game.media.group.PicGroup import PicGroup

dicesPicGroup = PicGroup(config.dicePics)


class Dice(Display):
    """
    骰子类
    """

    def __init__(self):
        """
        初始化 值和是否保留
        """
        self.value: int = 0
        self.isRemain: bool = False

        self.roll()

    def roll(self) -> None:
        """
        Roll 如果不保留就更换数值
        :return:
        """
        if not self.isRemain:
            self.value = randint(1, 6)

    def __int__(self) -> int:
        """
        定义转换为 int 的方法，就是返回bool
        :return: int
        """
        return self.value

    def __bool__(self) -> bool:
        """
        返回 isRemain
        :return:
        """
        return self.isRemain

    def toDisplayable(self):
        # todo 实现换图
        return dicesPicGroup[self.value - 1].toDisplayable()
