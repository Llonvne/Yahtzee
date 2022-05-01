import pygame.event
from pygame.event import Event as Event
from pygame.event import post as post

from events import *
from round import Round


def BlockUserInput():
    """
    该函数将会立刻阻断所有用户事件
    :return:
    """
    pygame.event.set_blocked((RemainK, RollNow, ChooseK))


def AllowUserInput():
    """
    该函数将允许所有用户事件通过
    :return:
    """
    pygame.event.set_blocked(None)


def ClearAllUserEventsInQueue():
    """
    该函数将会清除队列中所有用户事件
    :return:
    """
    pygame.event.clear((RemainK, RollNow, ChooseK))


def remainingK(k: int) -> None:
    """
    如果用户选择保留/不保留 第 K 个骰子，请立刻触发该事件
    :return:
    """
    post(Event(RemainK, {"用户事件": "保留第K个骰子", "remain": k}))


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


def processUserInput(event: Event, round: Round):
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
