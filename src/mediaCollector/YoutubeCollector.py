from utils.YoutubeScrapper import Scraper
from utils.YoutubeDownloader import MP3Downloader

class YoutubeCollector:
    """
    Collects MP3 files from YouTube using a combination of scraping and downloading.

    Attributes:
    - scraper (Scraper): An instance of the Scraper class for YouTube URL validation and extraction.
    - downloader (MP3Downloader): An instance of the MP3Downloader class for downloading MP3 files.

    Methods:
    - collect(input): Collects MP3 files based on the input provided, which can be a YouTube URL, a playlist URL, or a search query.
    """

    def __init__(self):
        """
        Initializes the YoutubeCollector with instances of Scraper and MP3Downloader.
        """
        self.scraper = Scraper()
        self.downloader = MP3Downloader()

    def collect(self, input):
        """
        Collects MP3 files based on the input provided.

        Parameters:
        - input (str): The input can be a YouTube URL, a playlist URL, or a search query.

        Returns:
        - tuple: A tuple containing a boolean indicating the success of the operation and either a single filename (if input is a URL or search query) or a list of filenames (if input is a playlist URL).
        """
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