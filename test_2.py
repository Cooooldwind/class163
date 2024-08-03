from class163 import Music
from pprint import pprint

m = Music("https://music.163.com/song?id=26201885&userid=1577080369")

pprint(
    m.get_file(
        offical=False,
        url=f"https://csm.sayqz.com/api/?type=apiSongUrlV1?level=lossless&id={m.id}&cookie=MUSIC_U=DEADBEEF1145141919810",
    )
)
