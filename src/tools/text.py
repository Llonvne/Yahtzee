# -*- coding = utf-8 -*-
# @Time : 2022/4/30 20:21
# @Author : daiwu
# @File : text.py
# @Software : PyCharm
import pygame.font


def displaytext(screen: pygame.surface, point, vlaue):
    star_x = 220
    star_y = 295
    lenth_x = 93
    lenth_y = 52
    Font = pygame.font.Font(pygame.font.get_default_font(), 30)
    Font_surface = Font.render(str(vlaue), True, (0, 0, 0), None)
    # screen.blit(Font_surface,(star_x+lenth_x*point[0],star_y+lenth_y*point[1]))
    screen.blit(Font_surface, (star_x, star_y))
