"""
This module implements the PlaylistManager class, which is basically the logic of a "playlist" made using circular doubly linked list.
It provides methods to interact with the playlist, such as adding songs, removing songs, changing the current song, and moving to the next or previous song.
We use this class in the MusicPlayer class to manage the playlist of songs.
this class also manages the MP3 inputs for soundController.py which is further imported in Player.py
"""


class SongNode:
    """
    Represents a song object as a node in a doubly linked list.
    """
    def __init__(self, mp3):
        """
        Initializes a SongNode with the given mp3 file.

        Parameters:
        - mp3 (str): The path to the MP3 file representing the song.
        """
        self.mp3 = mp3
        self.next_song = None
        self.prev_song = None

class PlaylistManager:
    """ 
    Implements the logic of a Playlist with the help of circular doubly linked list

    Implements the following methods:
        - addSongNode
        - removeSongNode
        - get_current_song_path
        - NextSong
        - PreviousSong
    """
    
    def __init__(self):
        """
        Initializes the PlaylistManager with the following attributes:

        Attributes:
        - head: The head of the circular doubly linked list representing the playlist. Initially set to None.
        - tail: The tail of the circular doubly linked list representing the playlist. Initially set to None.
        - current_song: A pointer that points to the song currently being played in the playlist. Initially set to None.
        - loop: A boolean flag indicating whether the playlist should loop back to the beginning after reaching the end. Default is True.
        """
        self.head = None
        self.tail = None
        self.current_song = self.head
        self.loop = True

    def addSongNode(self, mp3):
        '''
        Adds a SongNode to the Playlist.

        Parameters:
        - mp3 (str): The path to the MP3 file representing the song.

        '''
        new_song = SongNode(mp3)
        if not self.head and not self.tail: # if the queue is empty

            # Implementing circular doubly linked list
            # setting the next and previous pointers of the new song to itself 
            new_song.next_song = new_song
            new_song.prev_song = new_song
            self.head = self.tail = new_song
            
            # setting the current song to the first song in the queue
            self.current_song = new_song 

        else:
            self.tail.next_song = new_song
            new_song.prev_song = self.tail
            new_song.next_song = self.head
            self.tail = new_song
            self.head.prev_song = self.tail



    def removeSongNode(self):
        """
        Removes the head SongNode from the Playlist.
        """
        if not self.head:  # queue is empty
            return None
        elif self.head == self.tail:  # only one song in the queue
            dequeued_song = self.head
            self.head = self.tail = None
            self.current_song = None
        else:
            dequeued_song = self.head
            self.head = self.head.next_song
            self.head.prev_song = self.tail
            self.tail.next_song = self.head
        return dequeued_song.mp3 if dequeued_song else None

    def get_current_song_path(self):  # Updated method name
        '''
        Returns the path of the currently playing song, if it exists.

        Returns:
        - str: Path of the currently playing song (MP3) if it exists, None otherwise.
        '''
        if self.current_song:
            return (self.current_song.mp3) # returns .mp3 "str" of SongNode pointed by current_song
        else:
            return None # if the queue is empty

    def get_current_queue(self):
        """
        Returns a list of all the songs in the current playlist queue.

        Returns:
        - list: A list of the paths of all the songs in the current playlist queue.
        """
        if not self.head:  # queue is empty
            return []
        current = self.head
        queue = [current.mp3]
        while current.next_song != self.head:
            current = current.next_song
            queue.append(current.mp3)
        return queue
        
    def change_current_song(self, mp3):
        """
        Changes the current_song pointer to the song with the given mp3 path.

        Parameters:
        - mp3 (str): The path to the MP3 file representing the song.

        Returns:
        - bool: True if the song was found and the current_song pointer was updated, False otherwise.
        """
        if not self.head: # queue is empty
            return False
        current = self.head
        while current.mp3 != mp3:
            current = current.next_song
            if current == self.head: # if the song is not found
                return False
        self.current_song = current
        return True

    def NextSong(self):
        """
         Moves the current_song pointer to the next song in the playlist
         and returns the path of the new current_song (SongNode.mp3).
         
         Returns:
         - str or None: Path of the next song's MP3 if it exists, None otherwise.
        """
        if not self.head: # queue is empty
            return None
        if  not self.loop and self.tail.next_song == self.head: # if looping is disabled
            return None
        self.current_song = self.current_song.next_song
        return self.current_song.mp3

    def PreviousSong(self):
        """
        Moves the current_song pointer to the next song in the playlist
        and returns the path of the new current_song (SongNode.mp3).

        Returns:
        - str or None: Path of the next song's MP3 if it exists, None otherwise.
        """
        if not self.head: # queue is empty
            return None
        if not self.loop and self.head.prev_song == self.tail : # if looping is disabled
            return None
        self.current_song = self.current_song.prev_song
        return self.current_song.mp3
    
    def clear(self):
        """
        Clears the playlist by removing all the songs from the queue.
        """
        while self.head:
            self.removeSongNode()

    