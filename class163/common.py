from class163.origin_file import OriginFile

class BasicMusicType():

    def __init__(self):
        # 基本信息
        self.title: str = None
        self.subtitle: str = None
        self.artist: list[str] = None
        self.album: str = None
        # 歌词
        self.lyric: str = None
        # 文件
        self.music_file: OriginFile = None
        self.cover_file: OriginFile = None
        # 翻译信息
        self.trans_title: str = None
        self.trans_artist: list[str] = None
        self.trans_album: str = None
        self.trans_lyric: str = None

    def read(self, origin_dict: dict,
             title_keys: list = None,
             subtitle_keys: list = None,
             artist_keys: list = None,
             album_keys: list = None,
             trans_title_keys: list = None,
             trans_artist_keys: list = None,
             trans_album_keys: list = None,
             trans_lyric_keys: list = None,
             music_file_keys: list = None,
             cover_file_keys: list = None,):
        return_dict = {}
        if title_keys != None:
            temp_dict = origin_dict
            for temp_key in title_keys:
                temp_dict = temp_dict[temp_key]
            if temp_dict.class == str:
                self.title = temp_dict
                return_dict['title'] = self.title
        # ......
            