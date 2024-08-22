"""
class163/common.py
Version: 0.5.0*Unreleased
Author: CooooldWind_/马建仓AI助手@Gitee/豆包@字节跳动
E-Mail: 3091868003@qq.com
Copyright @CooooldWind_ / Following GNU_AGPLV3+ License
"""
from class163.origin_file import OriginFile
from typing import Optional, Dict, List, Union

class BasicMusicType():
    """
    表示基本音乐类型的类，用于从给定的字典中提取音乐相关信息并以特定格式返回。
    """

    def __init__(self):
        """
        初始化类的属性。
        """
        self.title = None
        self.subtitle = None
        self.artist = []
        self.album = None
        self.lyric = None
        self.music_file = None
        self.cover_file = None
        self.trans_title = None
        self.trans_artist = []
        self.trans_album = None
        self.trans_lyric = None

    def _extract_info(self, origin_dict: dict, keys: Union[List[str], str], expected_type) -> Optional[Union[str, OriginFile, list]]:
        """
        从给定的字典中通过一系列键提取信息，并检查提取出的值是否符合预期类型。
        如果符合预期类型则返回提取的值，否则返回 None。如果在提取过程中发生 KeyError 也返回 None。

        :param origin_dict: 原始字典。
        :param keys: 用于提取信息的键，可以是单个字符串或字符串列表。
        :param expected_type: 预期的返回值类型。
        :return: 提取出的符合预期类型的值或 None。
        """
        try:
            temp_dict = origin_dict
            for key in keys if isinstance(keys, list) else [keys]:
                temp_dict = temp_dict[key]
            if isinstance(temp_dict, expected_type):
                return temp_dict
        except KeyError:
            pass
        return None

    def write(self, origin_dict: dict, title_keys: Optional[List[str]] = None, subtitle_keys: Optional[List[str]] = None, artist_keys: Optional[List[str]] = None,
             artist_list_keys: Optional[List[str]] = None, album_keys: Optional[List[str]] = None, lyric_keys: Optional[List[str]] = None,
             trans_title_keys: Optional[List[str]] = None, trans_artist_keys: Optional[List[str]] = None, trans_artist_list_keys: Optional[List[str]] = None,
             trans_album_keys: Optional[List[str]] = None, trans_lyric_keys: Optional[List[str]] = None, music_file_keys: Optional[List[str]] = None,
             cover_file_keys: Optional[List[str]] = None) -> Optional[Dict]:
        """
        从给定的字典中提取音乐相关信息，并以字典形式返回。

        :param origin_dict: 包含音乐信息的原始字典。
        :param title_keys: 用于提取标题信息的键列表。
        :param subtitle_keys: 用于提取副标题信息的键列表。
        :param artist_keys: 用于提取艺术家信息的键列表。
        :param artist_list_keys: 用于提取艺术家列表信息的键列表。
        :param album_keys: 用于提取专辑信息的键列表。
        :param lyric_keys: 用于提取歌词信息的键列表。
        :param trans_title_keys: 用于提取翻译后标题信息的键列表。
        :param trans_artist_keys: 用于提取翻译后艺术家信息的键列表。
        :param trans_artist_list_keys: 用于提取翻译后艺术家列表信息的键列表。
        :param trans_album_keys: 用于提取翻译后专辑信息的键列表。
        :param trans_lyric_keys: 用于提取翻译后歌词信息的键列表。
        :param music_file_keys: 用于提取音乐文件 URL 的键列表。
        :param cover_file_keys: 用于提取封面文件 URL 的键列表。
        :return: 包含提取出的音乐信息的字典，如果没有提取到任何信息则返回 None。
        """
        return_dict = {}

        # 提取信息
        self.title = self._extract_info(origin_dict, title_keys, str)
        self.subtitle = self._extract_info(origin_dict, subtitle_keys, str)
        self.artist = [self._extract_info(tmp, artist_keys, str) for tmp in self._extract_info(origin_dict, artist_list_keys, list)]
        self.album = self._extract_info(origin_dict, album_keys, str)
        self.lyric = self._extract_info(origin_dict, lyric_keys, str)
        music_file_url = self._extract_info(origin_dict, music_file_keys, str)
        self.music_file = OriginFile(music_file_url) if music_file_url else None
        cover_file_url = self._extract_info(origin_dict, cover_file_keys, str)
        self.cover_file = OriginFile(cover_file_url) if cover_file_url else None
        self.trans_title = self._extract_info(origin_dict, trans_title_keys, str)
        self.trans_artist = [self._extract_info(tmp, trans_artist_keys, str) for tmp in self._extract_info(origin_dict, trans_artist_list_keys, list)]
        self.trans_album = self._extract_info(origin_dict, trans_album_keys, str)
        self.trans_lyric = self._extract_info(origin_dict, trans_lyric_keys, str)

        # 更新返回字典
        if self.title is not None:
            return_dict['title'] = self.title
        if self.subtitle is not None:
            return_dict['subtitle'] = self.subtitle
        if self.artist:
            return_dict['artist'] = self.artist
        if self.album is not None:
            return_dict['album'] = self.album
        if self.lyric is not None:
            return_dict['lyric'] = self.lyric
        if self.music_file:
            return_dict['music_file'] = self.music_file
        if self.cover_file:
            return_dict['cover_file'] = self.cover_file
        if self.trans_title is not None:
            return_dict['trans_title'] = self.trans_title
        if self.trans_artist:
            return_dict['trans_artist'] = self.trans_artist
        if self.trans_album is not None:
            return_dict['trans_album'] = self.trans_album
        if self.trans_lyric is not None:
            return_dict['trans_lyric'] = self.trans_lyric

        return return_dict if return_dict else None