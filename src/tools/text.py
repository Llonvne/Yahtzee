# -*- coding = utf-8 -*-
# @Time : 2022/4/30 20:21
# @Author : daiwu
# @File : text.py
# @Software : PyCharm
import pygame.font
def displaytext(screen: pygame.surface, point, vlaue,colorbool):
    # 用来判断颜色
    if colorbool:
        color = (0, 0, 0,)
    else:
        color = (156, 158, 161)
    if 0<=point[0]<=5:
        displaytop(screen, point, vlaue,color)
    elif point[0]==6:
        displaysubtotaln(screen, point, vlaue,color)
    elif point[0]==7:
        displayreword(screen, point, vlaue,color)
    elif point[0]==8:
        displayselsect(screen, point, vlaue, color)
    elif 9<=point[0]<=13:
        displaydown(screen, point, vlaue,color)
    else:
        displaytotal(screen, point, vlaue,color)


#用于输出第一部分的数字
def displaytop(screen: pygame.surface, point, vlaue,color):
    #用来判断初始坐标
    star_x = 207
    star_y = 143
    lenth_x = 81
    lenth_y = 35
    #字体样式的设计
    Font = pygame.font.Font(pygame.font.get_default_font(), 17)
    Font_surface = Font.render(str(vlaue), True,color, None)
    screen.blit(Font_surface,(star_x+lenth_x*point[1],star_y+lenth_y*point[0]))

#用于输出小节部分的数字
def displaysubtotaln(screen: pygame.surface, point, vlaue,color):
    #需要用到的颜色是 (228,226,227)
    star_x=211
    star_y=350
    lenth_x = 81
    Font = pygame.font.Font(pygame.font.get_default_font(), 14)
    Font_surface = Font.render(str(vlaue), True, color, None)
    screen.blit(Font_surface, (star_x + lenth_x * point[1], star_y))

def displayreword(screen: pygame.surface, point, vlaue,color):
    star_x=207
    star_y=383
    lenth_x = 81
    Font = pygame.font.Font(pygame.font.get_default_font(), 17)
    Font_surface = Font.render(str(vlaue), True, color, None)
    screen.blit(Font_surface, (star_x + lenth_x * point[1], star_y))

#输出全选部分数字
def displayselsect(screen: pygame.surface, point, vlaue,color):
    star_x=207
    star_y=438
    lenth_x = 81
    Font = pygame.font.Font(pygame.font.get_default_font(), 17)
    Font_surface = Font.render(str(vlaue), True, color, None)
    screen.blit(Font_surface, (star_x + lenth_x * point[1], star_y))

#输出底下部分的数字
def displaydown(screen: pygame.surface, point, vlaue,color):
    star_x=207
    star_y=481
    lenth_x = 81
    lenth_y = 35
    Font = pygame.font.Font(pygame.font.get_default_font(), 17)
    Font_surface = Font.render(str(vlaue), True, color, None)
    screen.blit(Font_surface, (star_x + lenth_x * point[1], star_y+lenth_y*(point[0]-9)))

def displaytotal(screen: pygame.surface, point, vlaue,color):
    if vlaue<100:
        star_x=205
    else:
        star_x = 195
    star_y=669
    lenth_x = 81
    Font = pygame.font.Font(pygame.font.get_default_font(), 22)
    Font_surface = Font.render(str(vlaue), True, color, None)
    screen.blit(Font_surface, (star_x + lenth_x * point[1], star_y))



