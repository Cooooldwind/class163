from class163 import Playlist
from pprint import pprint
"""
m = Music("https://music.163.com/song?id=1486506463&uct2=U2FsdGVk")
m.encode_session.set_cookies({"MUSIC_U": ""})
pprint(m.get(mode="dlf", level="lossless"))
    

from class163.playlist import Playlist
from pprint import pprint
pprint(Playlist(12323740535).get_detail())
"""
"""
from class163.search import Search
import json

U = "0A0DEADBEEF114514415411FEEDDAED0A0" # 但凡有点脑子就知道我不可能把我cookies发出来
with open("test.json", "w", encoding="UTF-8") as f:
    json.dump(
        Search(key="明透", search_type="song", cookie_dict={"MUSIC_U": U}).get(),
        fp=f, ensure_ascii=False
    )
"""

