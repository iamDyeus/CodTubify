import os
import tkinter as tk
from tkinter import Listbox
from pygame import mixer
import time

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Playlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None
        self.last_update_time = time.time()

    def add_song(self, song):
        new_node = Node(song)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.current = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.tail.next = self.head
            self.head.prev = self.tail

    def play_next(self):
        if self.current.next:
            self.current = self.current.next
            return self.current.data
        return None

    def play_previous(self):
        if self.current.prev:
            self.current = self.current.prev
            return self.current.data
        return None

    def add_new_songs(self, media_folder):
        current_time = time.time()
        if current_time - self.last_update_time < 10:  # Decreasing the number of times we check for new songs
            return

        self.last_update_time = current_time

        if os.path.exists(media_folder):
            for file in os.listdir(media_folder):
                if file.endswith(".mp3"):
                    song_path = os.path.join(media_folder, file)
                    if not self.song_in_playlist(song_path):
                        self.add_song(song_path)

    def song_in_playlist(self, song_path):
        current_node = self.head
        while True:
            if current_node.data == song_path:
                return True
            current_node = current_node.next
            if current_node == self.head:
                break
        return False

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("400x400")

        self.playlist = Playlist()
        self.load_songs()

        mixer.init()

        self.create_widgets()
        self.update_track_list()

    def load_songs(self):
        media_folder = "media/"
        if os.path.exists(media_folder):
            for file in os.listdir(media_folder):
                if file.endswith(".mp3"):
                    self.playlist.add_song(os.path.join(media_folder, file))

    def create_widgets(self):
        play_button = tk.Button(self.root, text="Play", command=self.play_music)
        play_button.pack(pady=10)

        pause_button = tk.Button(self.root, text="Pause", command=self.pause_music)
        pause_button.pack(pady=5)

        resume_button = tk.Button(self.root, text="Resume", command=self.resume_music)
        resume_button.pack(pady=5)

        stop_button = tk.Button(self.root, text="Stop", command=self.stop_music)
        stop_button.pack(pady=5)

        next_button = tk.Button(self.root, text="Next", command=self.play_next_song)
        next_button.pack(pady=5)

        prev_button = tk.Button(self.root, text="Previous", command=self.play_previous_song)
        prev_button.pack(pady=5)

        add_new_songs_button = tk.Button(self.root, text="Add New Songs", command=self.add_new_songs)
        add_new_songs_button.pack(pady=5)

        self.track_listbox = Listbox(self.root, selectmode=tk.SINGLE)
        self.track_listbox.pack(expand=True, fill="both", pady=10)

        # Binding double-click event to play selected song
        self.track_listbox.bind("<Double-Button-1>", self.double_click_play)

    def update_track_list(self):
        self.track_listbox.delete(0, tk.END)
        current_node = self.playlist.head
        while True:
            self.track_listbox.insert(tk.END, os.path.basename(current_node.data))
            current_node = current_node.next
            if current_node == self.playlist.head:
                break

    def play_music(self):
        current_song = self.playlist.current.data
        mixer.music.load(current_song)
        mixer.music.play()
        self.update_listbox_cursor()

    def pause_music(self):
        mixer.music.pause()

    def resume_music(self):
        mixer.music.unpause()

    def stop_music(self):
        mixer.music.stop()

    def play_next_song(self):
        next_song = self.playlist.play_next()
        if next_song:
            mixer.music.load(next_song)
            mixer.music.play()
            self.update_listbox_cursor()

    def play_previous_song(self):
        prev_song = self.playlist.play_previous()
        if prev_song:
            mixer.music.load(prev_song)
            mixer.music.play()
            self.update_listbox_cursor()

    def add_new_songs(self):
        media_folder = "media/"
        self.playlist.add_new_songs(media_folder)
        self.update_track_list()

    def double_click_play(self, event):
        selected_index = self.track_listbox.curselection()
        if selected_index:
            selected_song = self.track_listbox.get(selected_index)
            selected_song_path = os.path.join("media", selected_song)
            mixer.music.load(selected_song_path)
            mixer.music.play()
            self.update_listbox_cursor()

    def update_listbox_cursor(self):
        current_index = 0
        current_node = self.playlist.head
        while current_node != self.playlist.current:
            current_node = current_node.next
            current_index += 1
        self.track_listbox.selection_clear(0, tk.END)
        self.track_listbox.selection_set(current_index)
        self.track_listbox.see(current_index)

if __name__ == "__main__":
    root = tk.Tk()
    music_player = MusicPlayer(root)
    root.mainloop()
