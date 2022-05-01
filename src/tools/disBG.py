import os

import pygame


def disBg(screen: pygame.Surface) -> None:
    """
    在屏幕上显示默认背景，常用于刷新屏幕
    :param screen:
    :return: None
    """
    board = pygame.image.load(os.path.join('Media', 'Pic', 'board2.png'))
    roll = pygame.image.load(os.path.join('Media', 'Pic', 'ROLL0.png'))
    screen.blit(board, (0, 0))
    screen.blit(roll, (1075, 615))
