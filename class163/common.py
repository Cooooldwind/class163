"""
class163/common.py
Version: 0.5.0*Unreleased
Author: CooooldWind_/马建仓AI助手@Gitee/豆包@字节跳动
E-Mail: 3091868003@qq.com
Copyright @CooooldWind_ / Following GNU_AGPLV3+ License
"""
from typing import Optional, Dict, List, Union

class BasicMusicType:
    """
    表示基本音乐类型的类，用于从给定的字典中提取音乐相关信息并以特定格式返回。
    """

    def __init__(self):
        """
        初始化类的属性。
        """
        self.info = {}

    def extract(self, origin_dict: dict, keys: List[Union[str, int]], expected_type) -> Optional[Union[str, list]]:
        """
        从给定的字典中通过一系列键提取信息，并检查提取出的值是否符合预期类型。
        如果符合预期类型则返回提取的值，否则返回 None。如果在提取过程中发生 KeyError 也返回 None。

        :param origin_dict: 原始字典。
        :param keys: 用于提取信息的键。
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
