from src.data import ScoreBoard
from src.data.round import Round
from src.tools.disChoice import disChoice, disChoosed


class GameData:
    def __init__(self, screen):
        # 屏幕
        self.screen = screen

        # 初始化记分板
        self.scoreBoards = [ScoreBoard.Scoreboard(screen) for i in range(2)]

        # 初始化 轮 控制
        self.round = Round(self.scoreBoards)

    def displayScore(self):
        disChoice(self.round, self.screen)

    def displayChoosed(self, userNo):
        disChoosed(userNo, self.scoreBoards[userNo], self.screen)
