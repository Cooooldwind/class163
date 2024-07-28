import time
import pprint
from selenium import webdriver
from class163.playlist import Playlist
from netease_encode_api import EncodeSession

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
s = EncodeSession()
s.set_cookies(cookies)
p = Playlist("https://music.163.com/playlist?id=9269203337")
with open("result.json", "w+", encoding="UTF-8") as file:
    pprint.pprint(p.get(session=s), indent=2)
