from class163.origin_file import OriginFile

class BasicMusicType():

    def __init__(self):
        self.title = None
        self.subtitle = None
        self.artist = []
        self.album = None
        self.lyric = None
        self.music_file = None
        self.cover_file = None
        self.trans_title = None
        self.trans_artist = []
        self.trans_album = None
        self.trans_lyric = None

    def _extract_info(self, origin_dict, keys, expected_type):
        try:
            temp_dict = origin_dict
            for key in keys:
                temp_dict = temp_dict[key]
            if isinstance(temp_dict, expected_type):
                return temp_dict
        except KeyError:
            pass
        return None

    def write(self, origin_dict, title_keys=None, subtitle_keys=None, artist_keys=None,
             artists_keys=None, album_keys=None, lyric_keys=None,
             trans_title_keys=None, trans_artist_keys=None, trans_artists_keys=None,
             trans_album_keys=None, trans_lyric_keys=None, music_file_keys=None,
             cover_file_keys=None):

        return_dict = {}

        # 提取信息
        self.title = self._extract_info(origin_dict, title_keys, str)
        self.subtitle = self._extract_info(origin_dict, subtitle_keys, str)
        # ... 为其他属性重复上述过程 ...

        # 更新返回字典
        if self.title is not None:
            return_dict['title'] = self.title
        # ... 为其他属性重复上述过程 ...

        return return_dict

# fixed by 马建仓