"""
def extract_dict(nested_dict: dict, keys: list[str]):
    result = {}
    for key in keys:
        if key in nested_dict:
            result[key] = nested_dict[key]
        else:
            for value in nested_dict.values():
                if isinstance(value, dict):
                    sub_dict = extract_dict(value, [key])
                    if sub_dict:
                        result.update(sub_dict)
                        break
    return result
"""


def find_key(nested: dict | str | float | int | bool | list | None, key: list) -> str:
    if len(key) == 0:
        return nested
    else: return find_key(nested=nested[key[0]], key=key[1:])


def extract_info(raw_info: dict, url_key: list, md5_key: list, size_key: list):
    result = {
        "file_url": find_key(nested=raw_info, key=url_key),
        "file_md5": find_key(nested=raw_info, key=md5_key),
        "file_size": find_key(nested=raw_info, key=size_key),
    }
    return result


# 示例嵌套字典
sample_dict = {
    "code": 200,
    "data": [
        {
            "br": 1165055,
            "canExtend": False,
            "channelLayout": None,
            "code": 200,
            "effectTypes": None,
            "encodeType": "mp3",
            "expi": 1200,
            "fee": 0,
            "flag": 2064641,
            "freeTimeTrialPrivilege": {
                "remainTime": 0,
                "resConsumable": False,
                "type": 0,
                "userConsumable": False,
            },
            "freeTrialInfo": None,
            "freeTrialPrivilege": {
                "cannotListenReason": None,
                "freeLimitTagType": None,
                "listenType": None,
                "playReason": None,
                "resConsumable": False,
                "userConsumable": False,
            },
            "gain": -12.5542,
            "id": 26201885,
            "level": "lossless",
            "levelConfuse": None,
            "md5": "c44b3fa89133dfa5393213e7201e9ea2",
            "message": None,
            "payed": 0,
            "peak": 0.9919,
            "podcastCtrp": None,
            "rightSource": 0,
            "size": 38439049,
            "time": 263000,
            "type": "flac",
            "uf": None,
            "url": "http://m8.music.126.net/20240804085516/a149950481ac48120246e284fa0fc337/ymusic/69a2/c53f/d7f8/c44b3fa89133dfa5393213e7201e9ea2.flac",
            "urlSource": 0,
        }
    ],
}

# 测试函数

result_dict = extract_info(sample_dict, ["data",0,'url'], ['data',0,'md5'], ['data',0,'size'])
print(result_dict)
