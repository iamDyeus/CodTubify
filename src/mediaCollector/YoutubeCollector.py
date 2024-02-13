from utils.YoutubeScrapper import Scraper
from utils.YoutubeDownloader import MP3Downloader

class YoutubeCollector:
    def __init__(self):
        self.scraper = Scraper()
        self.downloader = MP3Downloader()

    def collect(self, input):
        if self.scraper.is_youtube_url(input):
            url = input
            success, filename = self.downloader.download_mp3(url)
            return success, filename
        elif self.scraper.is_playlist_url(input):
            playlist_links = self.scraper.get_playlist_items(input)
            success = True
            filenames = []
            for link in playlist_links:
                success, filename = self.downloader.download_mp3(link)
                if not success:
                    break
                filenames.append(filename)
            return success, filenames
        else:
            url = self.scraper.get_youtube_uri(input)
            if url:
                success, filename = self.downloader.download_mp3(url)
                return success, filename
            else:
                return False, None

