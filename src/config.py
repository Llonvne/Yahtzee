# 设置窗口大小，分辨率
import os

window_size: tuple = (1280, 720)
caption = "快艇骰子"

# 设置 LOGO
logo = os.path.join('Media', 'Pic', 'LOGO.jpeg')

# 设置默认 BGM
default_BGM = os.path.join('Media', 'Music', 'BGM.mp3')

# 设置 video
default_video_group = [os.path.join('Media', 'Video', 'Start0720.mp4'),
                       os.path.join('Media', 'Video', 'Start720.mp4')]

# 设置背景和 Logo 图片
background_path = os.path.join('Media', 'Pic', 'board2.png')
roll_path = os.path.join('Media', 'Pic', 'ROLL0.png')

# 骰子图片
dicePics: list = [(os.path.join('Media', 'Pic', '1.png')),
                  (os.path.join('Media', 'Pic', '2.png')),
                  (os.path.join('Media', 'Pic', '3.png')),
                  (os.path.join('Media', 'Pic', '4.png')),
                  (os.path.join('Media', 'Pic', '5.png')),
                  (os.path.join('Media', 'Pic', '6.png'))]
