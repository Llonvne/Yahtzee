from pygame import Surface

from src.board.Board import Board
from src.game.media.display.text import displaytext
from src.player.Player import Player


def displayChoice(player: Player, screen: Surface):
    """
    disChoice 封装接口
    :param player:
    :param screen:
    :return:
    """
    disChoice(player.board, player.diceBoard, player.no, screen)


def disChoice(board: Board, diceGroup, userNo, screen) -> None:
    # 显示 1
    if board.getScore('one') > 0:
        pass
    else:
        displaytext(screen, (0, userNo), diceGroup.countK(1), False)
    # 显示 2
    if board.getScore('two') > 0:
        pass
    else:
        displaytext(screen, (1, userNo), diceGroup.countK(2), False)
    # 显示 3
    if board.getScore('three') > 0:
        pass
    else:
        displaytext(screen, (2, userNo), diceGroup.countK(3), False)
    # 显示 4
    if board.getScore('four') > 0:
        pass
    else:
        displaytext(screen, (3, userNo), diceGroup.countK(4), False)
    # 显示 5
    if board.getScore('five') > 0:
        pass
    else:
        displaytext(screen, (4, userNo), diceGroup.countK(5), False)
    # 显示 6
    if board.getScore('six') > 0:
        pass
    else:
        displaytext(screen, (5, userNo), diceGroup.countK(6), False)
    # 显示全选
    if board.getScore('totalChoose') > 0:
        pass
    else:
        displaytext(screen, (8, userNo), diceGroup.total(), False)
    # 显示四骰同花
    if board.getScore('foursame') > 0:
        pass
    else:
        displaytext(screen, (9, userNo), diceGroup.fourSame(), False)
    # 显示葫芦
    if board.getScore('calabash') > 0:
        pass
    else:
        displaytext(screen, (10, userNo), diceGroup.calabash(), False)
    # 显示小顺
    if board.getScore('smallStraights') > 0:
        pass
    else:
        displaytext(screen, (11, userNo), diceGroup.smallStraights(), False)
    # 显示大顺
    if board.getScore('largeStraights') > 0:
        pass
    else:
        displaytext(screen, (12, userNo), diceGroup.largeStraights(), False)
    # 显示快艇
    if board.getScore('speedboat') > 0:
        pass
    else:
        displaytext(screen, (13, userNo), diceGroup.speedboat(), False)
