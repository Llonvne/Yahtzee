# 导入 pygame 托管类
from src.SpeedBoatDice_Beta_2.game.game import Game


class SpeedBoatDice:
    def __init__(self):
        # 初始化 pygame 托管类对象
        self.game = Game()
