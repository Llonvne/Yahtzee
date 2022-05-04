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

    def run(self):
        running = True

        # 回合内玩家编号
        inTermPlayerNo = 0

        while running:
            for event in self.game.getEventFromQueue():
                print(event)
                # 判断是不是退出
                if event.type == pygame.QUIT:
                    running = False
                    break
                # 处理鼠标按下事件
                if event.type == 1025:
                    mouse.event(event, self.game.postEvent)
                # 处理 Roll 事件
                if event.__dict__.get("类型") == "骰子事件" and event.__dict__.get('描述') == "投":
                    # 如果有机会就投
                    if self.players[inTermPlayerNo].isHasChance():
                        self.game.rollEffect.play()
                        self.players[inTermPlayerNo].roll()
                        for i in range(10):
                            self.players[inTermPlayerNo].rollNotCostChances()
                            self.game.wait(110)
                            self.game.screenUpdate(self.players)

                # 处理 选择事件
                if event.__dict__.get("类型") == "骰子事件" and event.__dict__.get('描述') == "选择":
                    # 获得编号
                    no: int = event.__dict__.get('no')
                    # 设置保留
                    self.players[inTermPlayerNo].setRemaining(no, not self.players[inTermPlayerNo].isRemain(no))
            # 调用 Game 处理屏幕更新
            self.game.screenUpdate(self.players)
