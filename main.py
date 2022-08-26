import re
from pytube import Playlist

class downloader:

    def yt_downloader(self):
        YOUTUBE_STREAM_AUDIO = input('Input stream ID(140 for mp3): ')  # modify the value to download a different stream
        DOWNLOAD_DIR = input(r'Input download path: ')
        url = input('Input YT Playlist URL: ')
        print(url)
        playlist = Playlist(url)

        # this fixes the empty playlist.videos list
        playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

        print(len(playlist.video_urls), 'videos in playlist')
        amount = len(playlist.video_urls)
        x=1
        for url in playlist.video_urls:
            print(url)

        for video in playlist.videos:
            print('Download started: downloading',x,'of',amount,'(',video,(''))
            x=x + 1
            audioStream = video.streams.get_by_itag(YOUTUBE_STREAM_AUDIO)
            audioStream.download(output_path=DOWNLOAD_DIR)
        print('Download finished')

Downloader = downloader()
Downloader.yt_downloader()
