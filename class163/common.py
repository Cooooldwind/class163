from class163.origin_file import OriginFile

class BasicMusicType():

    def __init__(self):
        # 基本信息
        self.title: str = None
        self.subtitle: str = None
        self.artist: list[str] = []
        self.album: str = None
        # 歌词
        self.lyric: str = None
        # 文件
        self.music_file: OriginFile = None
        self.cover_file: OriginFile = None
        # 翻译信息
        self.trans_title: str = None
        self.trans_artist: list[str] = []
        self.trans_album: str = None
        self.trans_lyric: str = None

    def read(self, origin_dict: dict,
             title_keys: list = None,
             subtitle_keys: list = None,
             artist_keys: list = None,
             artists_keys: list = None,
             album_keys: list = None,
             lyric_keys: list = None,
             trans_title_keys: list = None,
             trans_artist_keys: list = None,
             trans_artists_keys: list = None,
             trans_album_keys: list = None,
             trans_lyric_keys: list = None,
             music_file_keys: list = None,
             cover_file_keys: list = None,) -> dict:
        return_dict = {}
        # 标题
        if title_keys != None:
            temp_dict = origin_dict
            for temp_key in title_keys:
                temp_dict = temp_dict[temp_key]
            if temp_dict.class == str:
                self.title = temp_dict
                return_dict['title'] = self.title
        # 副标题
        if subtitle_keys != None:
            temp_dict = origin_dict
            for temp_key in subtitle_keys:
                temp_dict = temp_dict[temp_key]
            if temp_dict.class == str:
                self.subtitle = temp_dict
                return_dict['subtitle'] = self.subtitle
        # 歌手
        if artists_keys != None:
            temp_dict = origin_dict
            # 遍历找到歌手列表
            for temp_key in artists_keys:
                temp_dict = temp_dict[temp_key]
            # 确认是列表
            if temp_dict.class == list:
                artists_list = temp_dict
                # 遍历歌手
                for subject in artists_list:
                    temp_dict_2 = subject
                    if artist_keys != None:
                        # 找到歌手名称
                        for temp_key_2 in artist_keys:
                            temp_dict_2 = temp_dict_2[temp_key_2]
                        # 确认是字符串
                        if temp_dict_2.class == str:
                            self.artist.append(temp_dict_2)
                return_dict['artist'] = self.artist
        # 专辑
        if album_keys != None:
            temp_dict = origin_dict
            for temp_key in album_keys:
                temp_dict = temp_dict[temp_key]
            if temp_dict.class == str:
                self.album = temp_dict
                return_dict['album'] = self.album
        # 歌词
        if lyric_keys != None:
            temp_dict = origin_dict
            for temp_key in lyric_keys:
                temp_dict = temp_dict[temp_key]
            if temp_dict.class == str:
                self.lyric = temp_dict
                return_dict['lyric'] = self.lyric
        # 标题翻译
        if trans_title_keys != None:
            temp_dict = origin_dict
            for temp_key in trans_title_keys:
                temp_dict = temp_dict[temp_key]
            if temp_dict.class == str:
                self.trans_title = temp_dict
                return_dict['trans_title'] = self.trans_title
        # 歌手翻译
        if trans_artists_keys != None:
            temp_dict = origin_dict
            # 遍历找到歌手列表
            for temp_key in trans_artists_keys:
                temp_dict = temp_dict[temp_key]
            # 确认是列表
            if temp_dict.class == list:
                trans_artists_list = temp_dict
                # 遍历歌手
                for subject in trans_artists_list:
                    temp_dict_2 = subject
                    if trans_artist_keys != None:
                        # 找到歌手名称
                        for temp_key_2 in trans_artist_keys:
                            temp_dict_2 = temp_dict_2[temp_key_2]
                        # 确认是字符串
                        if temp_dict_2.class == str:
                            self.trans_artist.append(temp_dict_2)
                return_dict['trans_artist'] = self.trans_artist
        # 专辑翻译
        if trans_album_keys != None:
            temp_dict = origin_dict
            for temp_key in trans_album_keys:
                temp_dict = temp_dict[temp_key]
            if temp_dict.class == str:
                self.trans_album = temp_dict
                return_dict['trans_album'] = self.trans_album
        # 歌词翻译
        if trans_lyric_keys != None:
            temp_dict = origin_dict
            for temp_key in trans_lyric_keys:
                temp_dict = temp_dict[temp_key]
            if temp_dict.class == str:
                self.trans_lyric = temp_dict
                return_dict['trans_lyric'] = self.trans_lyric
        # 歌曲文件
        if music_file_keys != None:
            temp_dict = origin_dict
            for temp_key in music_file_keys:
                temp_dict = temp_dict[temp_key]
            if temp_dict.class == str:
                self.music_file = temp_dict
                return_dict['music_file'] = self.music_file
        # 封面文件
        if cover_file_keys != None:
            temp_dict = origin_dict
            for temp_key in cover_file_keys:
                temp_dict = temp_dict[temp_key]
            if temp_dict.class == str:
                self.cover_file = temp_dict
                return_dict['cover_file'] = self.cover_file
        return return_dict
            