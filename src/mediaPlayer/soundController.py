"""
This module implements the pygameController class, which is a wrapper around the pygame.mixer module.
It provides methods to interact with the pygame.mixer module, such as playing, stopping, pausing, unpausing, and changing the volume of a sound.
We use this class in the MusicPlayer class to control the playback of music.
"""

import pygame
import pygame.mixer as mixer

class pygameController:
    '''
    Class to interact with pygame.mixer
    Implements the following methods:
        - play
        - stop
        - pause
        - unpause
        - get_state
        - volume
        - lower_volume
        - raise_volume
        - change_directory
    '''
    def __init__(self, media_directory=None):
        try:
            mixer.init(44100, 32, 2, 2048)
        except pygame.error as e:
            print(f"Error initializing pygame mixer: {e}")
            return
        self.sounds_directory = media_directory

    def play(self, mp3):
        try:
            mixer.music.load(str(self.sounds_directory+str(mp3)))
            mixer.music.play()
        except pygame.error as e:
            print(f"Error loading or playing the MP3: {e}")

    def stop(self):
        try:
            mixer.music.stop()
        except pygame.error as e:
            print(f"Error stopping the music: {e}")

    def pause(self):
        try:
            if mixer.music.get_busy():
                mixer.music.pause()
            
        except pygame.error as e:
            print(f"Error pausing the music: {e}")

    def unpause(self):
        try:
            mixer.music.unpause()
        except pygame.error as e:
            print(f"Error unpausing the music: {e}")

    def get_state(self):
        try:
            return mixer.music.get_busy()
        except pygame.error as e:
            print(f"Error getting the state: {e}")
            return False

    @property
    def volume(self):
        try:
            return mixer.music.get_volume() * 100
        except pygame.error as e:
            print(f"Error getting the volume: {e}")
            return 0

    @volume.setter
    def volume(self, value):
        try:
            mixer.music.set_volume(value / 100)
        except pygame.error as e:
            print(f"Error setting the volume: {e}")

    def lower_volume(self):
        try:
            volume = mixer.music.get_volume()
            mixer.music.set_volume(max(0, volume - 0.1))
        except pygame.error as e:
            print(f"Error lowering the volume: {e}")

    def raise_volume(self):
        try:
            volume = mixer.music.get_volume()
            mixer.music.set_volume(min(1, volume + 0.1))
        except pygame.error as e:
            print(f"Error raising the volume: {e}")

    def change_directory(self, new_directory):
        self.sounds_directory = new_directory
        print(f"Changed directory to {new_directory}")
