from src.resetable.resetable import Resetable


class Board(Resetable):
    """
    分数类
    """
    def reset(self):
        for key in self.board.keys():
            self.board[key] = 0

    def __init__(self):
        self.board = {"one": 0, "two": 0, "three": 0, "four": 0, "five": 0, "six": 0,
                      "reward": 0, "totalChoose": 0, "foursame": 0, "calabash": 0, "smallStraights": 0,
                      "largeStraights": 0, "speedboat": 0}

    def totalScore(self):
        return sum([i[1] for i in self.board.items()])

    def numCount(self):
        i = 0
        sum = 0
        for s in self.board.items():
            if i < 6:
                i += 1
            else:
                break
            sum += s[1]
        return sum

    def addScore(self, scorename: str, score) -> None:
        self.board[scorename] += score

    def getScore(self, scorename: str) -> int:
        return self.board[scorename]
