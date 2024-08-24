"""
class163/common.py
Version: 0.5.1
Author: CooooldWind_/马建仓AI助手@Gitee/豆包@字节跳动
E-Mail: 3091868003@qq.com
Copyright @CooooldWind_ / Following GNU_AGPLV3+ License
"""

from typing import Optional, Dict, List, Union, Type


class BasicMusicType:
    """
    基础音乐类型处理类，提供从数据结构中提取信息的功能。
    """

    def __init__(self):
        self.title = None
        self.subtitle = None
        self.artist = []
        self.album = None
        self.trans_title = None
        self.trans_artist = []
        self.trans_album = None
        self.publish_time = []

    def info_dict(self) -> Dict:
        result = {
            "title": self.title,
            "subtitle": self.subtitle,
            "artist": self.artist,
            "album": self.album,
            "trans_title": self.trans_title,
            "trans_artist": self.trans_artist,
            "trans_album": self.trans_album,
            "publish_time": self.publish_time,
        }
        return result


def extract(
    origin: Dict, keys: List[Union[str, int]], expected_type: Type
) -> Optional[Union[str, list, int]]:
    """
    从字典中提取信息。

    :param origin: 源字典
    :param keys: 键列表
    :param expected_type: 期望的类型
    :return: 提取的结果，如果失败则返回 None
    """
    try:
        temp_dict = origin
        for key in keys:
            temp_dict = temp_dict[key]
        return temp_dict if isinstance(temp_dict, expected_type) else None
    except (KeyError, TypeError, IndexError):
        return None


def extract_in_list(
    origin: List[Optional[Dict]],
    keys: List[Union[str, int]],
    expected_type: Type,
) -> List:
    """
    在字典列表中提取信息。

    :param origin: 源字典列表
    :param keys: 键列表
    :param expected_type: 期望的类型
    :return: 提取结果的列表
    """
    return [extract(item, keys, expected_type) for item in origin]
