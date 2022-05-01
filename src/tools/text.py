# -*- coding = utf-8 -*-
# @Time : 2022/4/30 20:21
# @Author : daiwu
# @File : text.py
# @Software : PyCharm
import pygame.font


def displaytexttop(screen: pygame.surface, point, vlaue,colorbool):
    if colorbool:
        color=(156,158,161)
    else:
        color=(0,0,0,)
    star_x = 197
    star_y = 143
    lenth_x = 81
    lenth_y = 35
    Font = pygame.font.Font(pygame.font.get_default_font(), 21)
    Font_surface = Font.render(str(vlaue), True,color, None)
    screen.blit(Font_surface,(star_x+lenth_x*point[0],star_y+lenth_y*point[1]))

