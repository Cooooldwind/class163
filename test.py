import time
time_f, time_b = time.process_time(), time.process_time()
from pprint import pprint
from class163.music import Music, url_to_id
u = [
    "https://music.163.com/song?id=2086529025",
    "https://music.163.com/song?id=2097485069",
    "https://music.163.com/song?id=2040876720",
    "https://music.163.com/song?id=2085560360",
    "https://music.163.com/song?id=2149143970",
    "https://music.163.com/song?id=2146779694",
    "https://music.163.com/song?id=2145269432",
    "https://music.163.com/song?id=2045878963",
]

t = []
for i in u:
    m = Music(url_to_id(url = i))
    time_f = time.process_time()
    m.get()
    time_b = time.process_time()
    t.append(time_b - time_f)
    pprint(m.sorted_info)
print(t)