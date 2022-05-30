# -*- coding = utf-8 -*-
# @Time : 2022/5/30 15:23
# @Author : daiwu
# @File : displayPlayer.py
# @Software : PyCharm
import os.path

from src.game.media.types.pic import Pic


def displayer(game):
    player1=Pic(os.path.join('Media','Pic','player1.png'))
    player2=Pic(os.path.join('Media', 'Pic','player2.png'))
    game.display((player1,(180,37)))
    game.display((player2,(268,39)))

