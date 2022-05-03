# 导入 pygame 托管类
import pygame

from src.game.controller import mouse
from src.game.game import Game
from src.player.Player import Player


class SpeedBoatDice:
    def __init__(self):
        # 初始化 pygame 托管类对象
        self.game = Game()
        # 建立两个玩家
        self.players = [Player(i) for i in range(2)]
        # 推入开始事件
        self.game.postEvent("游戏进程控制", "游戏开始")
        self.players[0].isYourTerm = True
        self.players[0].roll()

    def run(self):
        running = True

        inTermPlayerNo = 0

        while running:
            for event in self.game.getEventFromQueue():
                print(event)
                # 判断是不是退出
                if event.type == pygame.QUIT:
                    running = False
                    break
                # 处理事件
                if event.type == 1025:
                    mouse.event(event, self.game.postEvent)
                # 处理 Roll 事件
                if event.__dict__.get("类型") == "骰子事件" and event.__dict__.get('描述') == "投":
                    if self.players[inTermPlayerNo].chance > 0:
                        self.players[inTermPlayerNo].diceBoard.roll()
                    self.players[inTermPlayerNo].chance -= 1
                # 处理 选择事件
                if event.__dict__.get("类型") == "骰子事件" and event.__dict__.get('描述') == "选择":
                    self.players[inTermPlayerNo].diceBoard.setRemaining(
                        event.__dict__.get('no'),
                        not self.players[inTermPlayerNo].diceBoard.isRemaining(event.__dict__.get('no'))
                    )
            self.game.display((self.game.backGround, (0, 0)))
            self.game.display((self.game.roll, (725, 600)))
            self.game.displayerScore(*self.players)
            if self.players[0].isYourTerm:
                self.game.displayDices(self.players[0].diceBoard.toDisplayable())
            else:
                self.game.displayDices(self.players[1].diceBoard.toDisplayable())
            self.game.screenUpdate()
            self.players[inTermPlayerNo].reset()
            inTermPlayerNo = 1 - inTermPlayerNo
