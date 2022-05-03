import pygame.event
from pygame.event import Event as Event

from src.data.round import Round
from src.events.events import *


def BlockUserInput():
    """
    该函数将会立刻阻断所有用户事件
    :return:

    # todo 该函数需要实现
    """
    # pygame.event.set_blocked((RemainK, RollNow, ChooseK))


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
    # todo 该函数需要实现


def remainingK(k: int) -> None:
    """
    如果用户选择保留/不保留 第 K 个骰子，请立刻触发该事件
    :return:
    """
    remainEvent(k)


def chooseKScore(k: int) -> None:
    """
    如果选择 第k个分数，请立刻触发该函数
    :param k:
    :return:
    """
    chooseKEvent(k)


def roll() -> None:
    """
    如果用户决定开始投骰子，请触发该函数
    :return:
    """
    RollStartEvent()


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
    if 1075 < event.__dict__.get('pos')[0] < 1075 + 105 and 615 < event.__dict__.get('pos')[1] < 615 + 81:
        print("123")
        roll()
