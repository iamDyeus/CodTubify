from mediaCollector.YoutubeCollector import YoutubeCollector 
from mediaPlayer.Player import MusicPlayer
import os
import time

def download(link, collector, player):
    success,filename = collector.collect(link)
    if success:
        player.add_to_playlist(filename) 
    return filename

def load_songs(player , directory="media"):
    queue = []
    for song in os.listdir(directory):
        if song.endswith(".mp3"):
            queue.append(song)
            player.add_to_playlist(song)
    return queue

if __name__ == '__main__':  
    collector = YoutubeCollector()
    player = MusicPlayer("pygame")
    links = ["https://www.youtube.com/watch?v=mpZrpOY7ABo","CNV Sound Vol 14"]
    
    # for link in links:
    #     download(link, collector, player)
    
    load_songs(player)

    print("\nCurrent playlist:")
    playlist = player.playlist.get_current_queue()
    for song in playlist:
        print("  - "+song[:30])

    player.play()
    print("\ncurrent song : "+player.playlist.get_current_song_path())
    time.sleep(10)

    player.play_next()
    print("\ncurrent song : "+player.playlist.get_current_song_path())
    time.sleep(10)
    
    player.play_next()
    print("\ncurrent song : "+player.playlist.get_current_song_path())
    time.sleep(10)