import pygame

from src import config
from src.game.media.display.disChoice import displayChoice
from src.game.media.display.display import Display
from src.game.media.display.text import displaytext
from src.game.media.types.effect import Effect
from src.game.media.types.music import Music
from src.game.media.types.pic import Pic
from src.game.media.types.video import Video
from src.player.Player import Player

"""
分数 str -> int 转换字典
"""
noToRead = {"one": 0, "two": 1, "three": 2, "four": 3, "five": 4, "six": 5,
            "smallCount": 6, "reward": 7, "totalChoose": 8, "foursame": 9,
            "calabash": 10, "smallStraights": 11, "largeStraights": 12,
            "speedboat": 13, "totalScore": 14}


class Game:
    """
    pygame API 托管类
    这个函数将会包装所有 pygame 接口
    所有对于 pygame 的操作都应该由该类托管，及其内部包装类托管

    event 处理需要实时性，在处理时直接使用 pygame.Event 而不进行包装
    """

    def __init__(self):
        """
        初始化游戏函数
        """
        # 初始化 pygame
        pygame.init()
        pygame.mixer.init()

        # 初始化标题
        pygame.display.set_caption(config.caption)

        # 初始化分辨率，获得显示对象
        self.screen = pygame.display.set_mode(config.window_size)

        # 设置 LOGO
        pygame.display.set_icon(
            pygame.image.load(config.logo)
        )

        # 播放视频
        if config.video_on:
            self.__videos = [Video(video_path).play() for video_path in config.default_video_group]

        # 播放 BGM
        if config.BGM_On:
            self.BGM = Music(config.default_BGM)
            self.BGM.play()

        # 显示 BG
        self.backGround = Pic(config.background_path)
        self.roll = Pic(config.roll_path)
        self.display((self.backGround, (0, 0)))
        self.display((self.roll, (900, 600)))

        # 初始化 投掷音效
        self.rollEffect = Effect(config.roll_effect_path)

        # 事件符号
        self.type = "类型"
        self.sub_type = "描述"

        # 动画帧率设置
        self._clock = pygame.time.Clock()

    def display(self, *displays: tuple[Display, tuple[int, int]]) -> None:
        """
        Display 类对应 显示接口
        调用 Display 类内部 toDisplayable 接口获得 pygame.Surface 对象，使用
        Surface.blit 接口进行显示
        :param displays:由 display 和 坐标组成的元组组成的元组
        :return: None
        """
        for display, pos in displays:
            """
            如果返回一个空元组，表示不显示
            """
            if isinstance(display.toDisplayable(), tuple):
                continue
            self.screen.blit(display.toDisplayable(), pos)

    def displayDices(self, display: list[tuple[Display, tuple[int, int]]]) -> None:
        """
        骰子列表对应显示接口
        内部具体有 display 接口实现
        :param display: 有 Display 对象和坐标组成的列表
        :return: None
        """
        for d in display:
            self.display((d[0], d[1]))

    @staticmethod
    def getEventFromQueue() -> list[pygame.event.Event]:
        """
        pygame.event.get() 对应包装接口
        获得事件队列
        :return: list[pygame.event.Event]
        """
        return pygame.event.get()

    def postEvent(self, type1, sub_type) -> None:
        """
        事件发生函数
        :param type1:
        :param sub_type:
        :return:
        """
        pygame.event.post(
            pygame.event.Event(pygame.USEREVENT, {self.type: type1, self.sub_type: sub_type})
        )

    def displayerScore(self, *players: Player):
        """
        分数显示函数
        :param players:
        :return:
        """
        # 获得回合内部玩家编号
        inTermPlayerNo = 0
        if players[1].isYourTerm:
            inTermPlayerNo = 1
        # 显示已经有的分数
        displayChoice(players[inTermPlayerNo], self.screen)
        # 显示可选择分数
        for v in players[inTermPlayerNo].board.isChoose.items():
            if players[inTermPlayerNo].board.isChoose[v[0]]:
                displaytext(self.screen, (noToRead[v[0]], inTermPlayerNo),players[inTermPlayerNo].board.getScore(v[0]), True)
        for v in players[1 - inTermPlayerNo].board.isChoose.items():
            if players[1 - inTermPlayerNo].board.isChoose[v[0]]:
                displaytext(self.screen, (noToRead[v[0]],1 - inTermPlayerNo),players[1 - inTermPlayerNo].board.getScore(v[0]), True)
        for i in range(2):
            # 显示小记
            displaytext(self.screen, (noToRead.get("smallCount"), i), players[i].board.numCount(),
                        True)
            # 显示总分
            displaytext(self.screen, (noToRead.get("totalScore"), i),
                        players[i].board.totalScore() + (35 if players[i].board.numCount() >= 63 else 0),
                        True)
            # 显示奖励
            displaytext(self.screen, (noToRead.get("reward"), i), (35 if players[i].board.numCount() >= 63 else 0),
                        True)

    def screenUpdate(self, players: list[Player]):
        """
        屏幕更新函数
        :param players: 玩家列表 用于显示玩家内部的骰子等
        :return:
        """

        # 显示背景
        self.display((self.backGround, (0, 0)))

        # 显示 Roll
        self.display((self.roll, (725, 600)))

        # 显示分数
        self.displayerScore(*players)

        # 显示当前玩家骰子
        if players[0].isYourTerm:
            self.displayDices(players[0].diceBoard.toDisplayable())
        else:
            self.displayDices(players[1].diceBoard.toDisplayable())

        # 更新屏幕
        self._clock.tick(config.fps)
        pygame.display.update()

    @staticmethod
    def wait(ms: int):
        """
        pygame.time.wait 函数包装接口
        :param ms:
        :return:
        """
        pygame.time.wait(ms)
