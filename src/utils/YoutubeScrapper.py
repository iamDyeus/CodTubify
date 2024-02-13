import re
import requests
from bs4 import BeautifulSoup
from youtube_search import YoutubeSearch
from pytube import Playlist

class Scraper:
    def __init__(self):
        pass

    YOUTUBE_URL_REGEX = re.compile(
        r'https?://(?:www\.)?(?:youtube\.com/watch\?v=|youtu\.be/)([^&=%\?]{11})'
    )
    YOUTUBE_PLAYLIST_REGEX = re.compile(
        r'https?://www.youtube.com/playlist\?list=([\w-]+)'
    )  

    @staticmethod
    def is_youtube_url(url):
        return bool(Scraper.YOUTUBE_URL_REGEX.match(url))
    
    @staticmethod
    def is_playlist_url(url):
        return bool(Scraper.YOUTUBE_PLAYLIST_REGEX.match(url))

    @staticmethod
    def get_title(url):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        title = soup.find('title')
        return title.text.removesuffix(' - YouTube')

    @staticmethod
    def get_youtube_uri(title):
        prefix = "https://www.youtube.com/watch?v="
        results = YoutubeSearch(title, max_results=1).to_dict()
        return prefix + results[0]["id"] if results else None

    @staticmethod
    def get_playlist_items(playlist_url):
        playlist = Playlist(playlist_url)
        print(f'Number Of Videos In playlist: {len(playlist.video_urls)}')
        prefix = "https://www.youtube.com/watch?v="
        return [prefix + video.video_id for video in playlist.videos]


# Example usage:
# scraper = Scraper()
# url = "https://www.youtube.com/watch?v=abcdefghijk"
# title = scraper.get_title(url)
# print(f"Title: {title}")

# uri = scraper.get_youtube_uri(title)
# print(f"YouTube URI: {uri}")

# playlist_url = "https://www.youtube.com/playlist?list=PLfP6i5T0-DkIMLNRwmJpRBs4PJvxfgwBg"
# playlist_links = scraper.get_playlist_items(playlist_url)
# print(f"Playlist Links: {playlist_links}")

# url_to_check = "https://www.youtube.com/watch?v=abcdefghijk"
# print(f"Is YouTube URL: {scraper.is_youtube_url(url_to_check)}")
