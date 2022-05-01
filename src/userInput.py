from pygame.event import Event as Event
from pygame.event import post as post

from events import *
from round import Round


def remainingK(k: int) -> None:
    """
    如果用户选择保留/不保留 第 K 个骰子，请立刻触发该事件
    :return:
    """
    post(Event(RemainK, {"用户事件": "保留第K个骰子", "remain": k}))


def toChooseScore() -> None:
    """
    如果用户选择去选择填入分数界面，请立刻触发该函数
    :return:
    """
    post(Event(ChooseScore, {"用户事件": "选择分数"}))


def toRoll() -> None:
    """
    如果用户选择去投骰子界面，请立刻触发该函数
    :return:
    """
    post(Event(Roll, {"用户事件": "投掷骰子界面"}))


def roll() -> None:
    """
    如果用户决定开始投骰子，请触发该函数
    :return:
    """
    post(Event(RollNow, {"用户事件": "投骰子"}))


def chooseKScore(k: int) -> None:
    """
    用户选择填入
    请注意 k 按照文字显示二维矩阵坐标，不需要返回用户 ID，只需要行号
    用户不应该选择小记，奖励分，总计分数
    :param k:
    :return: None
    """
    post(Event(ChooseK, {"用户事件": "记录第K个分数", "no": k}))


def processUserInput(event: Event, round:Round):
    """
    该函数用于不断接受各种事件，
    其中 event 为输入事件
    round 中
    isChooseable(self,k:int) 表示该分数是否可以选择
    请根据输入引发上述函数
    :param event:
    :param round:
    :return:
    """
