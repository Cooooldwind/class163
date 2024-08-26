import time
from tqdm import tqdm
from class163.playlist_old import Playlist
from netease_encode_api import EncodeSession
from class163.origin_file import OriginFile
from class163.music import artist_join
import qt_test

"""
driver = webdriver.ChromiumEdge()
driver.get("https://music.163.com/#/login/")
cookies = None
while True:
    cookies = driver.get_cookie("MUSIC_U")
    if cookies != None:
        cookies = {cookies["name"]: cookies["value"]}
        driver.close()
        break
    else:
        time.sleep(0.5)
"""
s = EncodeSession()
c = qt_test.login()
s.set_cookies(c)
p = Playlist("https://music.163.com/playlist?id=9097772489")
p.get(detail=False, session=s)
for m in p.track[0:5]:
    m.get("dlf", session=s, level="standard")
    of = OriginFile(m.file_url)
    of.begin_download(multi_thread=True)
    while of.get_percentage() < 100.0:
        with tqdm(
            total=of.tot_size,
            unit="b",
            desc=f"Downloading: {m.title} - {artist_join(m.artist)}",
        ) as t:
            t.update(of.now_size)
    with open(f"{m.title} - {artist_join(m.artist)}.mp3", "wb") as f:
        f.write(of.data)
    with open(f"{m.title} - {artist_join(m.artist)}.lrc", "w+", encoding="UTF-8") as f:
        f.write(m.lyric)
