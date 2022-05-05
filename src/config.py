# 设置窗口大小，分辨率
import os

window_size: tuple = (1280, 720)
caption = "快艇骰子"

# 设置 LOGO
logo = os.path.join('Media', 'Pic', 'LOGO.jpeg')

# 设置默认 BGM
BGM_On = True
default_BGM = os.path.join('Media', 'Music', 'BGM.mp3')

# Roll Effect_path
roll_effect_path = os.path.join('Media','Music','touziD.mp3')

# 设置 video
video_on = True
default_video_group = [os.path.join('Media', 'Video', 'Start0720.mp4'),
                       os.path.join('Media', 'Video', 'Start720.mp4')]

# 设置背景和 Logo 图片
background_path = os.path.join('Media', 'Pic', 'board2.png')
roll_path = os.path.join('Media', 'Pic', 'RollPic2.png')

# 骰子图片
dicePics: list = [(os.path.join('Media', 'Pic', '11.png')),
                  (os.path.join('Media', 'Pic', '22.png')),
                  (os.path.join('Media', 'Pic', '33.png')),
                  (os.path.join('Media', 'Pic', '44.png')),
                  (os.path.join('Media', 'Pic', '55.png')),
                  (os.path.join('Media', 'Pic', '66.png'))]

remainDicesPics: list[str] = [(os.path.join('Media', 'Pic', 'one.png')),
                              (os.path.join('Media', 'Pic', 'two.png')),
                              (os.path.join('Media', 'Pic', 'three.png')),
                              (os.path.join('Media', 'Pic', 'four.png')),
                              (os.path.join('Media', 'Pic', 'five.png')),
                              (os.path.join('Media', 'Pic', 'six.png'))]

# FPS
fps = 10
