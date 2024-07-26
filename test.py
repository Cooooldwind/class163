from class163.music import Music
from pprint import pprint
m = Music("https://music.163.com/song?id=1839931917")
m.encode_session.set_cookies()