import pygame
from src.round import Round
from src.tools.text import displaytext


def disChoice(round:Round, screen: pygame.Surface) -> None:
    """
    Display the choice of dice to be kept.
    :param diceGroup:
    :param scoreBoard:
    :param userNo:
    :param screen:
    :return:
    """
    userNo = round.userNo
    scoreBoard = round.scoreBoard[round.userNo]
    diceGroup = round.diceGroup
    # 显示 1
    if scoreBoard.one > 0:
        displaytext(screen, (0, userNo), scoreBoard.one, True)
    else:
        displaytext(screen, (0, userNo), diceGroup.countK(1), False)
    # 显示 2
    if scoreBoard.two > 0:
        displaytext(screen, (1, userNo), scoreBoard.two, True)
    else:
        displaytext(screen, (1, userNo), diceGroup.countK(2), False)
    # 显示 3
    if scoreBoard.three > 0:
        displaytext(screen, (2, userNo), scoreBoard.three, True)
    else:
        displaytext(screen, (2, userNo), diceGroup.countK(3), False)
    # 显示 4
    if scoreBoard.four > 0:
        displaytext(screen, (3, userNo), scoreBoard.four, True)
    else:
        displaytext(screen, (3, userNo), diceGroup.countK(4), False)
    # 显示 5
    if scoreBoard.five > 0:
        displaytext(screen, (4, userNo), scoreBoard.five, True)
    else:
        displaytext(screen, (4, userNo), diceGroup.countK(5), False)
    # 显示 6
    if scoreBoard.six > 0:
        displaytext(screen, (5, userNo), scoreBoard.six, True)
    else:
        displaytext(screen, (5, userNo), diceGroup.countK(6), False)
    # 显示全选
    if scoreBoard.total > 0:
        displaytext(screen, (8, userNo), scoreBoard.total, True)
    else:
        displaytext(screen, (8, userNo), diceGroup.total(), False)
    # 显示四骰同花
    if scoreBoard.fourSame > 0:
        displaytext(screen, (9, userNo), scoreBoard.fourSame(), True)
    else:
        displaytext(screen, (9, userNo), diceGroup.fourSame(), False)
    # 显示葫芦
    if scoreBoard.calabash > 0:
        displaytext(screen, (10, userNo), scoreBoard.calabash(), True)
    else:
        displaytext(screen, (10, userNo), diceGroup.calabash(), False)
    # 显示小顺
    if scoreBoard.smallStraights > 0:
        displaytext(screen, (11, userNo), scoreBoard.smallStraights(), True)
    else:
        displaytext(screen, (11, userNo), diceGroup.smallStraights(), False)
    # 显示大顺
    if scoreBoard.largeStraights > 0:
        displaytext(screen, (12, userNo), scoreBoard.largeStraights(), True)
    else:
        displaytext(screen, (12, userNo), diceGroup.largeStraights(), False)
    # 显示快艇
    if scoreBoard.speedboat > 0:
        displaytext(screen, (13, userNo), scoreBoard.speedboat(), True)
    else:
        displaytext(screen, (13, userNo), diceGroup.speedboat(), False)
