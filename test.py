import time
from pprint import pprint
from selenium import webdriver
from class163.music import Music

#  driver = webdriver.Safari() -> NoSuchDriverException
driver = webdriver.Edge()
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
#  pprint(cookies)
m = Music("https://music.163.com/song?id=1839931917")
m.encode_session.set_cookies(cookies)
pprint(m.get_file(level = "exhigh"))