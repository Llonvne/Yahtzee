from src.board.Board import Board
from src.game.media.display.text import displaytext


def disChoice(board: Board, diceGroup, userNo, screen) -> None:
    # 显示 1
    if board.board.get('one') > 0:
        pass
    else:
        displaytext(screen, (0, userNo), diceGroup.countK(1), False)
    # 显示 2
    if board.board.get('two') > 0:
        pass
    else:
        displaytext(screen, (1, userNo), diceGroup.countK(2), False)
    # 显示 3
    if board.board.get('three') > 0:
        pass
    else:
        displaytext(screen, (2, userNo), diceGroup.countK(3), False)
    # 显示 4
    if board.board.get('four') > 0:
        pass
    else:
        displaytext(screen, (3, userNo), diceGroup.countK(4), False)
    # 显示 5
    if board.board.get('five') > 0:
        pass
    else:
        displaytext(screen, (4, userNo), diceGroup.countK(5), False)
    # 显示 6
    if board.board.get('six') > 0:
        pass
    else:
        displaytext(screen, (5, userNo), diceGroup.countK(6), False)
    # 显示全选
    if board.board.get('totalChoose') > 0:
        pass
    else:
        displaytext(screen, (8, userNo), diceGroup.total(), False)
    # 显示四骰同花
    if board.board.get('foursame') > 0:
        pass
    else:
        displaytext(screen, (9, userNo), diceGroup.fourSame(), False)
    # 显示葫芦
    if board.board.get('calabash') > 0:
        pass
    else:
        displaytext(screen, (10, userNo), diceGroup.calabash(), False)
    # 显示小顺
    if board.board.get('smallStraights') > 0:
        pass
    else:
        displaytext(screen, (11, userNo), diceGroup.smallStraights(), False)
    # 显示大顺
    if board.board.get('largeStraights') > 0:
        pass
    else:
        displaytext(screen, (12, userNo), diceGroup.largeStraights(), False)
    # 显示快艇
    if board.board.get('speedboat') > 0:
        pass
    else:
        displaytext(screen, (13, userNo), diceGroup.speedboat(), False)
