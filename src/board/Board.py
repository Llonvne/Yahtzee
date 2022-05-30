from src.resetable.resetable import Resetable


class Board(Resetable):
    """
    分数板类
    继承 Resetable类以提供reset接口
    负责统计分数
    """

    def reset(self) -> None:
        """
        Resetable reset 抽象接口
        实现 Board 重制
        :return: None
        """
        for key in self.__board.keys():
            self.__board[key] = 0

    def __init__(self):
        """
        初始化板各项分数为 0
        """
        self.__board = {"one": 0, "two": 0, "three": 0, "four": 0, "five": 0, "six": 0,
                        "reward": 0, "totalChoose": 0, "foursame": 0, "calabash": 0, "smallStraights": 0,
                        "largeStraights": 0, "speedboat": 0}
        self.isChoose = {"one": False, "two": False, "three": False, "four": False, "five": False, "six": False,
                         "reward": False, "totalChoose": False, "foursame": False, "calabash": False,
                         "smallStraights": False, "largeStraights": False, "speedboat": False}

    def totalScore(self) -> int:
        """
        返回所有的分数总和
        :return:int
        """
        return sum([i[1] for i in self.__board.items()])

    def numCount(self) -> int:
        """
        返回单数字分数总和
        :return: int
        """
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
        """
        添加分数，接受两个参数，分数名称 str, 添加的分数值 int
        :param scorename:
        :param score:
        :return: None
        """
        self.__board[scorename] += score

    def getScore(self, scorename: str) -> int:
        """
        获得分数
        :param scorename: 分数名称
        :return: 分数值
        """
        return self.__board[scorename]

    def getScores(self):
        """
        获得 分数名：分数 _dict_items 对象
        :return:
        """
        return self.__board.items()
