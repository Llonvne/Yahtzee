import pygame

from src import config
from src.game.media.display.disChoice import disChoice
from src.game.media.display.display import Display
from src.game.media.display.text import displaytext
from src.game.media.types.music import Music
from src.game.media.types.pic import Pic
from src.player.Player import Player

noToRead = {"one": 0, "two": 1, "three": 2, "four": 3, "five": 4, "six": 5,
            "smallCount": 6, "reward": 7, "totalChoose": 8, "foursame": 9,
            "calabash": 10, "smallStraights": 11, "largeStraights": 12,
            "speedboat": 13, "totalScore": 14}


class Game:
    """
    pygame API 托管类
    这个函数将会包装所有 pygame 接口
    所有对于 pygame 的操作都应该由该类托管
    """

    def __init__(self):
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
        # self.__videos = [Video(video_path).play() for video_path in config.default_video_group]

        # 播放 BGM
        self.BGM = Music(config.default_BGM)
        self.BGM.play()

        # 显示 BG
        self.backGround = Pic(config.background_path)
        self.roll = Pic(config.roll_path)
        self.display((self.backGround, (0, 0)))
        self.display((self.roll, (725, 600)))

        # 事件符号
        self.type = "类型"
        self.sub_type = "描述"

    def display(self, *displays: tuple[Display, tuple[int, int]]) -> None:
        """
        显示图像
        :param displays:由 display 和 坐标组成的元组
        :return:
        """
        for display, pos in displays:
            self.screen.blit(display.toDisplayable(), pos)

    def displayDices(self, display: list[tuple[Display, tuple[int, int]]]):
        for d in display:
            self.display((d[0], d[1]))

    @staticmethod
    def getEventFromQueue():
        return pygame.event.get()

    def postEvent(self, type1, sub_type, **kwargs):
        pygame.event.post(
            pygame.event.Event(pygame.USEREVENT, {self.type: type1, self.sub_type: sub_type, **kwargs})
        )

    def displayerScore(self, *players: Player):
        # 显示已经有的分数
        for player in players:
            if player.isYourTerm:
                disChoice(player.board, player.diceBoard,player.no,self.screen)
                for score in player.board.board.items():
                    if score[1] > 0:
                        displaytext(self.screen, (noToRead[score[0]], player.no), score[1], True)
        for i in range(2):
            displaytext(self.screen, (noToRead.get("smallCount"), i), players[i].board.numCount(),
                        True)
            displaytext(self.screen, (noToRead.get("totalScore"), i),
                        players[i].board.totalScore() + (35 if players[i].board.numCount() >= 63 else 0),
                        True)
            displaytext(self.screen, (noToRead.get("reward"), i), (35 if players[i].board.numCount() >= 63 else 0),
                        True)

    @staticmethod
    def screenUpdate():
        pygame.display.update()
