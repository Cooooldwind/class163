"""
class163/common.py
Version: 0.5.0*Unreleased
Author: CooooldWind_/马建仓AI助手@Gitee/豆包@字节跳动
E-Mail: 3091868003@qq.com
Copyright @CooooldWind_ / Following GNU_AGPLV3+ License
"""
from typing import Optional, Dict, List, Union

class BasicMusicType:

    def __init__(self):
        self.info = {}

    def extract(self, origin_dict: dict, keys: List[Union[str, int]], expected_type) -> Optional[Union[str, list]]:
        try:
            temp_dict = origin_dict
            for key in keys if isinstance(keys, list) else [keys]:
                temp_dict = temp_dict[key]
            if isinstance(temp_dict, expected_type):
                return temp_dict
        except KeyError:
            pass
        return None
