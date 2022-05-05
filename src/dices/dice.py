from random import randint

from src import config
from src.game.media.display.display import Display
from src.game.media.group.PicGroup import PicGroup

# 加载未保留骰子图像
dicesPicGroup = PicGroup(config.dicePics)
# 加载被保留的骰子图像
remainPicGroup = PicGroup(config.remainDicesPics)


class Dice(Display):
    """
    骰子类
    """

    def __init__(self):
        """
        初始化 值和是否保留
        """
        self.__value: int = 0
        self.isRemain: bool = False

        # Roll 保证骰子数值正常
        self.roll()

    def roll(self) -> None:
        """
        Roll 如果不保留就更换数值
        :return:
        """
        if not self.isRemain:
            self.__value = randint(1, 6)

    def __int__(self) -> int:
        """
        定义转换为 int 的方法，就是返回bool
        :return: int
        """
        return self.__value

    def __bool__(self) -> bool:
        """
        返回 isRemain
        :return:
        """
        return self.isRemain

    def toDisplayable(self):
        """
        Display 接口 显示接口
        :return: pygame.Surface 对象
        """
        if self.isRemain:
            return remainPicGroup[self.__value - 1].toDisplayable()
        return dicesPicGroup[self.__value - 1].toDisplayable()

    def getValue(self) -> int:
        """
        获得骰子的值
        :return: int 骰子的值
        """
        return self.__value
