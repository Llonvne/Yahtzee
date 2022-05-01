# 播放视频
from moviepy.video.io.VideoFileClip import VideoFileClip


def play():
    start0Video = VideoFileClip("Media/Video/Start0720.mp4").subclip(0, 3.3)
    startVideo = VideoFileClip("Media/Video/Start720.mp4").subclip(0, 2.4)
    start0Video.preview()
    startVideo.preview()
    startVideo.close()
    start0Video.close()
