"""
class163/music.py
Version: 0.3.7
Author: CooooldWind_
E-Mail: 3091868003@qq.com
Copyright @CooooldWind_ / Following GNU_AGPLV3+ License
"""

from typing import Literal
from typing_extensions import TypeAlias


class GlobalArgs:
    def __init__(self):
        self.FILE_URL = "https://music.163.com/weapi/song/enhance/player/url/v1"
        self.LYRIC_URL = "https://music.163.com/weapi/song/lyric"
        self.DETAIL_URL = "https://music.163.com/weapi/v3/song/detail"
