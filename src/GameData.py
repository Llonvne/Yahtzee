from src.GameItem import ScoreBoard
from src.round import Round
from src.tools.disChoice import disChoice


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
