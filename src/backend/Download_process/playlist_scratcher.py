#scratch links from a youtube playlist url
from pytube import Playlist


def get_playlist_items(playlist_url):
    plylst_links=[]
    playlist = Playlist(playlist_url)
    print('Number Of Videos In playlist: %s' % len(playlist.video_urls))
    for video in playlist.videos:
        suffix=video.video_id
        prefix="https://www.youtube.com/watch?v="
        plylst_links.append(prefix+suffix)
    return plylst_links


# Playlist Links :
#coding :
#lofi : https://www.youtube.com/playlist?list=PLfP6i5T0-DkIMLNRwmJpRBs4PJvxfgwBg
#bass : https://www.youtube.com/playlist?list=PL6vFaUSqVjRnYH6iULv1WzcK4V0d-S1t-



