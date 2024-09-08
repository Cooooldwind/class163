import class163
from class163.common import attribute_write_mp3, cover_write_mp3, artist_join
from pprint import pprint
import time


U = "008443F3DF9F5A6F0A8F638821B48019CDCB621665D591FA6EFBDFE00392A0EFC8DA91F4642C6522DE753250B917B3AB0CF377AF0CF193FC484D96D4789CABCA168F7A6FAADFD5C9796C45E7E9DEFE46D2AF9E5F2B30281A5D84ACAFE7AC60525EF91A88A33A9E2F52E193BF9F95EFA0CE99BCBE6780B3E687345DAC802E0627FBF08DE63D72208ACAB06B1B9BE5326DCFDFBDDAB474BB5FFF8625219E9AB8D61F9FF3D9E0864CCB25F316D6686830FB2237A83B6DBBDB548F860BDD004F55DCA6D475B94178952677730C56E16E15F973A17D85D63F3C3A64A5D6121C548DC65B9488A3CBDE493B52C1C641908D94C5A9D0402E24A0DDC93B47121B7633F7FD417B15A07DC9B40E25CE1404890DDF7F7A2132F576625A91B591A06381AE3D12B8787CC02235D05AD218E1ED4FC2AE8C1763D3DE8A56548F217BDAC8BD01264CCFBADB8D2AF6DE77E295EE2BE05608C7AF12B4CA772C927E81F714EA0DC7F3CF80"
p = class163.Playlist("https://music.163.com/playlist?id=12324368073&uct2=U2FsdGVkX1+iWMf7o5A0wCSRMz6UMa3+1uuMfiYzz0o=")
p.encode_session.set_cookies({"MUSIC_U": ""})
print("Loading...", end="")
p.get_detail(each_music=False)
tot_size = 0
for m in p.track:
    m.__init__(m.id)
    m.encode_data_update()
    m.encode_session.set_cookies({"MUSIC_U": U})
    m.get(mode="dlf", level="exhigh")
    m.cover_file = class163.OriginFile(f"{m.cover_file_url}?param=800y800")
    tot_size += m.cover_file.tot_size
    tot_size += m.music_file.tot_size
print(f"\"{p.title}\" by {p.creator} is loaded.")
print(f"Needed Size: {tot_size / 1024 / 1024}MB.")
print("Start.")
for m in p.track:
    m.music_file.begin_download(multi_thread=True)
    while m.music_file.get_percentage() < 100.0:
        print(f"{m.title} - {artist_join(m.artist, ", ")} | {m.music_file.get_percentage()}%")
        time.sleep(0.5)
    m.cover_file.begin_download(multi_thread=True)
    while m.cover_file.get_percentage() < 100.0:
        print(f"{m.title} - {artist_join(m.artist, ", ")} | {m.cover_file.get_percentage()}%")
        time.sleep(0.5)
    music_file_bytes = m.music_file.get_data()
    music_file_bytes = attribute_write_mp3(file=music_file_bytes, attribute=m.info_dict())
    music_file_bytes = cover_write_mp3(file=music_file_bytes, cover=m.cover_file.get_data())
    with open(f"C:/Users/Administrator/Downloads/ncmld_downloads/{m.title} - {artist_join(m.artist, ", ")}.mp3", mode="wb") as f:
        f.write(music_file_bytes)
    with open(f"C:/Users/Administrator/Downloads/ncmld_downloads/{m.title} - {artist_join(m.artist, ", ")}.lrc", mode="w", encoding="UTF-8") as f:
        if m.lyric != None:
            f.write(m.lyric)
    print(f"{m.title} - {artist_join(m.artist, ", ")} OK")