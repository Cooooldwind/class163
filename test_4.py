"""
from class163.music import Music
from pprint import pprint
pprint(Music("https://music.163.com/song?id=1486506463&uct2=U2FsdGVkX19PImPHgQ0/67dW7Hj62Hj3yxx/OEBK8pA=").get_detail())
"""
from class163.playlist import Playlist
from pprint import pprint
pprint(Playlist(12323740535).get_detail())