import pygame

from GameItem import ScoreBoard
from GameItem.DiceGroup import DiceGroup
from text import displaytext


def disChoice(diceGroup: DiceGroup, scoreBoard: ScoreBoard,
              userNo: int, screen: pygame.Surface) -> None:
    """
    Display the choice of dice to be kept.
    :param diceGroup:
    :param scoreBoard:
    :param userNo:
    :param screen:
    :return:
    """
    # 显示 1
    if scoreBoard.one > 0:
        displaytext(screen, (0, userNo), 0)
    else:
        displaytext(screen, (0, userNo), diceGroup.countK(1))
    # 显示 2
    if scoreBoard.two > 0:
        displaytext(screen, (1, userNo), 0)
    else:
        displaytext(screen, (1, userNo), diceGroup.countK(2))
    # 显示 3
    if scoreBoard.three > 0:
        displaytext(screen, (2, userNo), 0)
    else:
        displaytext(screen, (2, userNo), diceGroup.countK(3))
    # 显示 4
    if scoreBoard.four > 0:
        displaytext(screen, (3, userNo), 0)
    else:
        displaytext(screen, (3, userNo), diceGroup.countK(4))
    # 显示 5
    if scoreBoard.five > 0:
        displaytext(screen, (4, userNo), 0)
    else:
        displaytext(screen, (4, userNo), diceGroup.countK(5))
    # 显示 6
    if scoreBoard.six > 0:
        displaytext(screen, (5, userNo), 0)
    else:
        displaytext(screen, (5, userNo), diceGroup.countK(6))
    # 显示小记
    displaytext(screen, (6, userNo), scoreBoard.totalScoreofNumber())
    # 显示奖励分
    displaytext(screen, (7, userNo), scoreBoard.reward)
    # 显示全选
    displaytext(screen, (8, userNo), scoreBoard.total)
    # 显示四骰同花
    displaytext(screen, (9, userNo), scoreBoard.fourSame)
    # 显示葫芦
    displaytext(screen, (10, userNo), scoreBoard.calabash)
    # 显示小顺
    displaytext(screen, (11, userNo), scoreBoard.smallStraight)
    # 显示大顺
    displaytext(screen, (12, userNo), scoreBoard.largeStraights)
    # 显示快艇
    displaytext(screen, (13, userNo), scoreBoard.speedboat)
    # 显示总分
    displaytext(screen, (14, userNo), scoreBoard.totalScore())
