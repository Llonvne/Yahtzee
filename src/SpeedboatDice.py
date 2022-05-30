# 导入 pygame 托管类
import pygame

from src import config
from src.game.controller import mouse
from src.game.controller.chooseScore import chooseScore
from src.game.game import Game
from src.game.media.types.pic import Pic
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
        # 回合计数
        self.termCount = 1

    def run(self):
        running = True

        goodGame = False

        # 回合内玩家编号
        inTermPlayerNo = 0
        winnerID: int = 0

        while running:
            for event in self.game.getEventFromQueue():
                print(event)
                # 判断是不是退出
                if event.type == pygame.QUIT:
                    running = False
                    break

                if event.__dict__.get("类型") == "游戏流程控制时间" and event.__dict__.get('描述') == '游戏结束':
                    if self.players[1].board.totalScore() > self.players[0].board.totalScore():
                        winnerID = 1
                    if winnerID == 0:
                        self.game.display((Pic(config.win_pic_path),(190,50)))
                    else:
                        self.game.display((Pic(config.win_pic_path), (270, 50)))
                    pygame.display.update()
                    goodGame = True

                if goodGame:
                    continue
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

                # 处理 分数选择 时间
                if event.__dict__.get('类型') == '分数选择':
                    chooseScore(self.players[inTermPlayerNo], event)
                if event.__dict__.get('类型') == '游戏流程控制事件' and event.__dict__.get('描述') == '玩家选择分数完毕':
                    if inTermPlayerNo == 1 and self.termCount == 12:
                        self.game.postEvent("游戏流程控制时间", "游戏结束")
                    self.players[inTermPlayerNo].isYourTerm = False
                    self.players[1 - inTermPlayerNo].isYourTerm = True
                    inTermPlayerNo = 1 - inTermPlayerNo
                    self.players[inTermPlayerNo].resetInTerm()
                    if inTermPlayerNo == 0:
                        self.termCount += 1
            # 调用 Game 处理屏幕更新
            if goodGame:
                if winnerID == 0:
                    self.game.display((Pic(config.win_pic_path), (190, 50)))
                else:
                    self.game.display((Pic(config.win_pic_path), (270, 50)))
            self.game.screenUpdate(self.players)
