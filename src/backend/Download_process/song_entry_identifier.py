def is_youtube_url(url):
    if "https://www.youtube.com/watch?v=" in url:
        return True
    elif "https://youtu.be/" in url:
        return True
    else:
        return False