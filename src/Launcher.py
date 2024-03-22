from mediaCollector.YoutubeCollector import YoutubeCollector 
from mediaPlayer.Player import MusicPlayer
import os
from mediaPlayer.soundController import pygameController

def download(link, collector, player):
    success,filename = collector.collect(link)
    if success:
        player.add_to_playlist(filename) 
    return filename

def load_songs(directory, player):
    for song in os.listdir(directory):
        # print(song+" added to playlist from dir "+directory)
        player.add_to_playlist(song)

if __name__ == '__main__':
    sound = pygameController()
    collector = YoutubeCollector()
    player = MusicPlayer("pygame")
    links = ["https://www.youtube.com/watch?v=5qap5aO4i9A"]
    
    # for link in links:
        # download(link, collector, player)
    
    load_songs("media", player)

    print("\nCurrent playlist:")
    playlist = player.playlist.get_current_queue()
    for song in playlist:
        print("  - "+song[:30])

    print("\ncurrent song  directory :")
    print(player.playlist.get_current_song_path())

    player.play_simple()

    # try:
    #     player.play_simple()
    # except Exception as e:
    #     print("Error:", e)


