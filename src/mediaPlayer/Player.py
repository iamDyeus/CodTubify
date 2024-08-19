from .soundController import pygameController
from .mediaManager import PlaylistManager
import pygame
import threading
import ctypes

class MusicPlayer:
    def __init__(self, mixer="pygame", music="media/"):
        """
        Initializes the MusicPlayer with the specified mixer type.

        Args:
        - mixer (str): The type of mixer to use. Only "pygame" is stable for now.
        - music (str): The directory where music files are stored.

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
        self.isManuallyPaused = False

        # Load the music files in the media directory
        self.load_songs()

        # Initialize the Pygame display to use the event system
        pygame.display.init()
        pygame.display.set_mode((1, 1))

        # Hide the Pygame window on Windows
        hwnd = pygame.display.get_wm_info()["window"]
        ctypes.windll.user32.ShowWindow(hwnd, 0)  # 0 = SW_HIDE

        # Define a custom event for song end
        self.SONG_END = pygame.USEREVENT + 1
        pygame.mixer.music.set_endevent(self.SONG_END)
        
        self.event_thread = None
        self.stop_event_thread = threading.Event()

        # Callback for song change, used to send a callback for Updating the GUI
        self.on_song_change = None

    def set_on_song_change_callback(self, callback):
        """Sets the callback function to be called when the song changes."""
        self.on_song_change = callback
    
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
        Plays the current song in the playlist if no argument is provided.

        Parameters:
        - mp3 (str): The path to the MP3 file to play. If provided, the current song in the playlist is changed to this MP3 file.

        Uses:
        - PlaylistManager.change_current_song method to change the current song in the playlist.
        - PlaylistManager.get_current_song_path method to get the path of the current song in the playlist.
        - sound_controller.play method to play the MP3 file.
        """
        if mp3:
            self.playlist.change_current_song(mp3)

        # Notify about the song change
        if self.on_song_change:
            self.on_song_change(self.playlist.get_current_song_path())
        # Play the Song
        self.sound_controller.play(self.playlist.get_current_song_path())

        # Start the event thread if not already running (For automatic playing nextSong after one song ends)
        if self.event_thread is None or not self.event_thread.is_alive():
            self.stop_event_thread.clear()
            self.event_thread = threading.Thread(target=self.run_event_loop, daemon=True)
            self.event_thread.start()

    def stop(self):
        self.sound_controller.stop()
        self.playlist.clear()
        self.stop_event_thread.set()  # Stop the event thread

    def reset_playlist(self):
        self.playlist.clear()
        
    def pause(self):
        self.isManuallyPaused = True
        self.sound_controller.pause()

    def unpause(self):
        self.isManuallyPaused = False
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
        directory = kwargs.get("dir", self.directory)
        import os
        songs = os.listdir(directory)
        for song in songs:
            if song.endswith(".mp3"):
                self.add_to_playlist(song)

    def run_event_loop(self):
        """
        Made for continuous play of songs in the playlist. It is a daemon thread that runs in the background to play the next song in the playlist when the current song ends.
        """
        while not self.stop_event_thread.is_set():
            for event in pygame.event.get():
                if event.type == self.SONG_END:
                    self.play_next()
            pygame.time.wait(150)  # Add a small delay to prevent high CPU usage
