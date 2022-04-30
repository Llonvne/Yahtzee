import os

import pygame


def disBg(screen: pygame.Surface) -> None:
    board = pygame.image.load(os.path.join('Media', 'Pic', 'board2.png'))
    screen.blit(board, (0, 0))
