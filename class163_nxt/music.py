"""
class163/music.py
Version: 0.10.0
Author: CooooldWind_
E-Mail: 3091868003@qq.com
Copyright @CooooldWind_ / Following GNU_AGPLV3+ License
"""

import time

from typing import Literal
from typing_extensions import TypeAlias
from urllib.parse import urlparse, parse_qs
from netease_encode_api import EncodeSession

# 歌曲音质/文件类型(aac -> m4a/flac, mp3 -> mp3/flac)
LEVEL: TypeAlias = Literal["standard", "higher", "exhigh", "lossless"]
MUSIC_FILE_TYPE: TypeAlias = Literal["mp3", "aac"]

FILE_URL = "https://music.163.com/weapi/song/enhance/player/url/v1"
LYRIC_URL = "https://music.163.com/weapi/song/lyric"
DETAIL_URL = "https://music.163.com/weapi/v3/song/detail"

def url_to_id(url: str) -> str:
    """
    从给定的 URL 中提取歌曲 ID。

    :param url: 包含歌曲 ID 的 URL。

    :return: 提取出的歌曲 ID。
    """
    try:
        parsed_url = urlparse(url)
        query_params = parse_qs(parsed_url.query)
        song_id = query_params.get("id", [None])[0]
        if song_id is not None:
            return str(song_id)
        else:
            raise ValueError("URL 中未找到 'id' 参数")
    except (ValueError, TypeError) as e:
        raise e

class Music:
    def __init__(self, id: int|str):
        """
        初始化 Music 类实例。

        :param id: 音乐的 ID，可以是整数或字符串。如果是包含"music.163.com"的 URL，则从 URL 中提取歌曲 ID。
        """
        self.id: int = 0
        self.title: str = ""                # 标题
        self.subtitles: list[str] = []      # 副标题 (可能会有一大堆?)
        self.artist: list[str] = []         # 艺术家
        self.album: str = ""                # 专辑
        self.trans_title: str = ""          # 标题译名
        self.trans_artist: list[str] = []   # 艺术家译名
        self.trans_album: str = ""          # 专辑译名
        # 发布时间
        self.publish_time: time.struct_time = time.localtime(0)
        self.cover_url: str = ""
        self.cover_bytes: bytes = bytes()   # 封面数据
        self.music_url: str = ""
        self.music_bytes: bytes = bytes()   # 音乐数据
        self.lyric: str = ""                # 歌词
        self.trans_lyric: str = ""          # 歌词翻译
        """
        # 详细信息请求的加密前数据
        self.__detail_encode_data = {"c": str([{"id": self.id}])}
        # 歌词信息请求的加密前数据
        self.__lyric_encode_data = {"id": self.id,"lv": -1,"tv": -1,}
        # 歌曲文件请求的加密前数据
        self.__file_encode_data = {
            "ids": str([self.id]),
            "level": ,              # standard/higher/exhigh/lossless/?????
            "encodeType": ,            # aac/mp3
        }
        """

    def get_info(self,
                 # 加密会话
                 encode_session: EncodeSession = EncodeSession(),
                 level: LEVEL = "standard", # 音质
                 lyric: bool = True,        # 歌词
                 cover: bool = True,        # 封面
                 music: bool = True         # 文件
                 ) -> dict|None:
        """
        获取音乐信息。
        
        :param encode_session: 加密会话 (来自netease_encode_api)
            - 请记得在 encode_session 里面先行填入用户凭证

        :param level: 音质 (standard/higher/exhigh/lossless/...)
        
            - standard: 标准 (mp3, 128kbps, 一首约3MB)
            - higher: 较高 (mp3, 192kbps, 一首约5MB)
            - exhigh: 极高 (mp3, 320kbps, 一首约10MB)
            - lossless: 无损 (flac, 无码率限制, 一首可能达到100MB+)
            - 超清母带等 SVIP 专用音质正在适配...

        :param lyric: 歌词获取 (True/False)
        :param cover: 专辑封面获取 (True/False)
        :param music: 歌曲源文件获取 (True/False)

        :return: 包含歌曲信息的字典
        """
        detail_encode_data = {"c": str([{"id": str(self.id)}])}
        raw_detail = encode_session.get_response(url = DETAIL_URL, encode_data = detail_encode_data)["songs"][0]
        self.title = raw_detail["name"]
        self.subtitles = raw_detail["alia"]
        self.album = raw_detail["al"]["name"]
        self.trans_title = raw_detail["al"]["tns"][0]
        self.trans_album = raw_detail["al"]["tns"]
        # 艺术家
        artist_list: list[dict] = raw_detail["ar"]
        self.artist = [tmp["name"] for tmp in artist_list]
        self.trans_artist = [tmp["tns"] for tmp in artist_list]
        # 发布时间
        self.publish_time = time.localtime(raw_detail["publishTime"])
        # 专辑封面
        self.cover_url = raw_detail["al"]["picUrl"]
        if lyric:
            lyric_encode_data = {"id": str(self.id),"lv": -1,"tv": -1}
            raw_detail = encode_session.get_response(url = DETAIL_URL, encode_data = detail_encode_data)
            self.lyric = raw_detail["lrc"]["lyric"]
            self.trans_lyric = raw_detail["tlyric"]["lyric"]
        self.cover_bytes: bytes = bytes()   # 封面数据
        self.music_bytes: bytes = bytes()   # 音乐数据
        
        
