from abc import ABC, abstractmethod
from typing import Dict

# 定义音乐数据模型类
class MusicData:
    """
    表示音乐数据的类，包含歌曲 ID、标题和艺术家信息
    """
    def __init__(self, id: str, title: str, artist: str):
        """
        初始化音乐数据对象

        :param id: 歌曲 ID
        :param title: 歌曲标题
        :param artist: 歌曲艺术家
        """
        self.id = id
        self.title = title
        self.artist = artist

# 定义抽象的音乐数据源接口
class MusicDataSource(ABC):
    """
    抽象基类，定义了音乐数据源应实现的获取歌曲详情和歌词的方法
    """
    @abstractmethod
    def get_song_detail(self, song_id: str) -> MusicData:
        """
        抽象方法，获取指定歌曲 ID 的详情

        :param song_id: 歌曲 ID
        :return: 包含歌曲详情的 MusicData 对象
        """
        pass

    @abstractmethod
    def get_lyrics(self, song_id: str) -> str:
        """
        抽象方法，获取指定歌曲 ID 的歌词

        :param song_id: 歌曲 ID
        :return: 歌词字符串
        """
        pass

# 网易云音乐数据源实现
class NetEaseMusicDataSource(MusicDataSource):
    """
    网易云音乐数据源的具体实现类
    """
    def get_song_detail(self, song_id: str) -> MusicData:
        """
        模拟获取网易云音乐的歌曲详情

        :param song_id: 歌曲 ID
        :return: 包含模拟详情的 MusicData 对象
        """
        # 模拟获取网易云音乐的歌曲详情
        return MusicData(song_id, f"Title from NetEase for {song_id}", "Artist from NetEase")

    def get_lyrics(self, song_id: str) -> str:
        """
        模拟获取网易云音乐的歌词

        :param song_id: 歌曲 ID
        :return: 模拟的歌词字符串
        """
        # 模拟获取网易云音乐的歌词
        return f"Lyrics from NetEase for {song_id}"

# 音乐数据处理类
class MusicDataProcessor:
    """
    处理音乐数据的类，使用注入的数据源来获取和处理数据
    """
    def __init__(self, data_source: MusicDataSource):
        """
        初始化音乐数据处理器

        :param data_source: 音乐数据源对象
        """
        self.data_source = data_source

    def process_song(self, song_id: str):
        """
        处理指定歌曲 ID 的音乐数据，获取详情和歌词并打印

        :param song_id: 歌曲 ID
        """
        song_detail = self.data_source.get_song_detail(song_id)
        lyrics = self.data_source.get_lyrics(song_id)
        print(f"Song ID: {song_detail.id}, Title: {song_detail.title}, Artist: {song_detail.artist}, Lyrics: {lyrics}")

# 配置和使用
data_source = NetEaseMusicDataSource()
processor = MusicDataProcessor(data_source)
processor.process_song("12345")
