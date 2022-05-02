import os

from src.events.events import *
from src.events.handler.EventHandler import EventHandler
from src.tools.text import displaytext

board = pygame.image.load(os.path.join('Media', 'Pic', 'board2.png'))
roll = pygame.image.load(os.path.join('Media', 'Pic', 'ROLL0.png'))


def disBg(screen: pygame.Surface) -> None:
    """
    在屏幕上显示默认背景，常用于刷新屏幕
    :param screen:
    :return: None
    """
    screen.blit(board, (0, 0))
    screen.blit(roll, (1075, 615))


class ScreenController(EventHandler):

    def event(self, event: pygame.event.Event):
        # 屏幕刷新事件
        if self.get_sub_type(event) == ScreenRefreshEvent:
            pygame.display.update()
        # 显示背景事件
        if self.get_sub_type(event) == DisplayBackgroundEvent:
            self.disBGandRoll()
            # 显示分数事件
        if self.get_sub_type(event) == DisplayInfoEvent:
            # 显示选择的小分
            self.data.displayChoosed(1 - self.data.round.userNo)
            self.data.displayScore()
            for userNo in range(2):
                # 显示奖励分
                if self.data.scoreBoards[userNo].isReward() >= 63:
                    displaytext(self.data.screen, (7, userNo), 35, True)
                else:
                    displaytext(self.data.screen, (7, userNo), 0, True)
                # 显示小记
                displaytext(self.data.screen, (6, userNo),
                            self.data.scoreBoards[userNo].totalScoreofNumber(), True)
                # 显示总分
                displaytext(self.data.screen, (14, userNo),
                            self.data.scoreBoards[userNo].totalScore(), True)
            # 调用屏幕刷新事件，刷新屏幕
            screenRefreshEvent()
        elif self.get_sub_type(event) == DisplayDicesEvent:
            self.data.round.diceGroup.displayDices(self.data.screen)
            screenRefreshEvent()

    def disBGandRoll(self):
        disBg(self.data.screen)
