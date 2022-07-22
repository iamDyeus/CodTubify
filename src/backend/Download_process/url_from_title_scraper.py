#scratch youtube URL from Title
from youtube_search import YoutubeSearch


def get_youtube_uri(title):
    prefix = "https://www.youtube.com/watch?v="
    results = YoutubeSearch(title, max_results=1).to_dict()
    if results:
        suffix = results[0]["id"]
        return prefix+suffix
    return None

