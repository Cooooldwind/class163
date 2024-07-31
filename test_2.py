from class163 import Music
from pprint import pprint

m = Music("https://music.163.com/song?id=26201885&userid=1577080369")
pprint(m.get(mode="dfl", level="exhigh"), sort_dicts=False)
