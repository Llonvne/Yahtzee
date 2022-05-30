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
    if board.isChoose['one']:
        pass
    else:
        displaytext(screen, (0, userNo), diceGroup.countK(1), False)
    # 显示 2
    if board.isChoose['two']:
        pass
    else:
        displaytext(screen, (1, userNo), diceGroup.countK(2), False)
    # 显示 3
    if board.isChoose['three']:
        pass
    else:
        displaytext(screen, (2, userNo), diceGroup.countK(3), False)
    # 显示 4
    if board.isChoose['four']:
        pass
    else:
        displaytext(screen, (3, userNo), diceGroup.countK(4), False)
    # 显示 5
    if board.isChoose['five']:
        pass
    else:
        displaytext(screen, (4, userNo), diceGroup.countK(5), False)
    # 显示 6
    if board.isChoose['six']:
        pass
    else:
        displaytext(screen, (5, userNo), diceGroup.countK(6), False)
    # 显示全选
    if board.isChoose['totalChoose']:
        pass
    else:
        displaytext(screen, (8, userNo), diceGroup.total(), False)
    # 显示四骰同花
    if board.isChoose['foursame']:
        pass
    else:
        displaytext(screen, (9, userNo), diceGroup.fourSame(), False)
    # 显示葫芦
    if board.isChoose['calabash']:
        pass
    else:
        displaytext(screen, (10, userNo), diceGroup.calabash(), False)
    # 显示小顺
    if board.isChoose['smallStraights']:
        pass
    else:
        displaytext(screen, (11, userNo), diceGroup.smallStraights(), False)
    # 显示大顺
    if board.isChoose['largeStraights']:
        pass
    else:
        displaytext(screen, (12, userNo), diceGroup.largeStraights(), False)
    # 显示快艇
    if board.isChoose['speedboat']:
        pass
    else:
        displaytext(screen, (13, userNo), diceGroup.speedboat(), False)
