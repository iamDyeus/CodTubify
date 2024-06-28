from .soundController import pygameController
from .mediaManager import PlaylistManager

class MusicPlayer:
    def __init__(self, mixer="pygame", music="media/"):
        """
        Initializes the MusicPlayer with the specified mixer type.

        Parameters:
        - mixer (str): The type of mixer to use. Only "pygame" is stable for now.

        Raises:
        - ValueError: If an invalid mixer type is provided.
        """
        self.directory = music
        if mixer == "pygame":
            self.sound_controller = pygameController(media_directory=music)
        else:
            self.sound_controller = pygameController(media_directory=music)
            raise ValueError("Invalid mixer type. Please use 'pygame'")
        self.playlist = PlaylistManager()
        # load the music files in the media directory
        self.load_songs()

    def add_to_playlist(self, mp3):
        """
        when a song is downloaded, it is added to the playlist using this method

        Parameters:
        - mp3 (str): The path to the MP3 file to add to the playlist.

        Uses:
        - PlaylistManager.enqueue method to add the MP3 file to the playlist.
        """
        self.playlist.addSongNode(mp3)

    def play(self, mp3=None):
        """
        # Method to Play Songs
        plays the current song in the playlist if no argument is provided
        
        Parameters:
        - mp3 (str): The path to the MP3 file to play. If provided, the current song in the playlist is changed to this MP3 file.
        
        Uses:
        - PlaylistManager.change_current_song method to change the current song in the playlist.
        - PlaylistManager.get_current_song_path method to get the path of the current song in the playlist.
        - sound_controller.play method to play the MP3 file.
        """
        if mp3:
            self.playlist.change_current_song(mp3)
        self.sound_controller.play(self.playlist.get_current_song_path())

        # Set end event to play next song
        # This will play the next song in the playlist when the current song ends
        self.sound_controller.after_song_ends(self.play_next)

    def stop(self):
        self.sound_controller.stop()
        self.playlist.clear()

    def reset_playlist(self):
        self.playlist.clear()
        
    def pause(self):
        self.sound_controller.pause()

    def unpause(self):
        self.sound_controller.unpause()

    def is_playing(self):
        return self.sound_controller.get_state()

    @property
    def volume(self):
        return self.sound_controller.volume

    @volume.setter
    def volume(self, value):
        self.sound_controller.volume = value

    def lower_volume(self):
        self.sound_controller.lower_volume()

    def play_next(self):
        self.play(self.playlist.NextSong())

    def play_previous(self):
        self.play(self.playlist.PreviousSong())

    def load_songs(self, **kwargs):
        """
        this method will load all the songs present in the directory
        Its main usecase is to load all the previously downloaded songs into the player
        """
        import os
        
        if("dir" in kwargs):
            dir = kwargs["dir"]
        else : dir = self.directory

        songs = os.listdir(dir)
        for song in songs :
            if song.endswith(".mp3"):
                self.add_to_playlist(song)
        