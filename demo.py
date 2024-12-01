from tqdm import tqdm
from class163 import Playlist
from netease_encode_api import EncodeSession
from class163.origin_file import OriginFile
from class163.common import artist_join, clean
import qt_test

def download_songs(playlist_url):
    p = Playlist(playlist_url)
    s = EncodeSession()
    s.set_cookies(qt_test.login())
    p.get_detail(session=s)

    for m in p.track:
        m.get("dlf", session=s, level="exhigh")
        fn = clean(f"{m.title} - {artist_join(m.artist)}")
        of = OriginFile(m.file_url)
        of.begin_download(multi_thread=True)

        while of.get_percentage() < 100.0:
            with tqdm(
                total=of.tot_size,
                unit="b",
                desc=f"Downloading: {fn}",
            ) as t:
                t.update(of.now_size)

# 主程序，提示用户输入歌单链接并下载歌曲
playlist_url = input("请输入歌单链接：")
download_songs(playlist_url)
