from src.resetable.resetable import Resetable


class Board(Resetable):
    """
    分数类
    """

    def reset(self):
        for key in self.__board.keys():
            self.__board[key] = 0

    def __init__(self):
        self.__board = {"one": 0, "two": 0, "three": 0, "four": 0, "five": 0, "six": 0,
                        "reward": 0, "totalChoose": 0, "foursame": 0, "calabash": 0, "smallStraights": 0,
                        "largeStraights": 0, "speedboat": 0}

    def totalScore(self):
        return sum([i[1] for i in self.__board.items()])

    def numCount(self):
        i = 0
        sum = 0
        for s in self.__board.items():
            if i < 6:
                i += 1
            else:
                break
            sum += s[1]
        return sum

    def addScore(self, scorename: str, score) -> None:
        self.__board[scorename] += score

    def getScore(self, scorename: str) -> int:
        return self.__board[scorename]

    def getScores(self):
        return self.__board.items()
