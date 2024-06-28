from pathlib import Path
import threading
from tkinter import *
import os


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# I Used this method earlier to load the songs from the directory
# But for not fucking up my brain again with directory and stuff
# I am rather using the Playlist from my PLAYER class
# which returns all the SongNodes present in the mixer queue
# Working with Directories is FUCKED UP!
def load_songs_dir(Listbox, directory="media"):
    """
    Loads Songs in the ListBox from the "/media" Directory
    """
    Listbox.delete(0, END) # Clear List first
    for song in os.listdir(directory):
        if song.endswith(".mp3"):
            Listbox.insert(END, song)


class Playlist(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.canvas = Canvas(
            self,
            bg = "#FFFFFF",
            height = 500,
            width = 675,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        self.canvas.place(x = 0, y = 0)


        # IMAGES FOR THE PLAYLIST GUI
        self.img_rect_bar = PhotoImage(file=relative_to_assets("image_2.png"))
        self.img_playlist_bg = PhotoImage(file=relative_to_assets("image_1.png"))
        self.img_btn_play = PhotoImage(file=relative_to_assets("button_1.png"))
        self.img_btn_refresh = PhotoImage(file=relative_to_assets("button_2.png"))


        # Creating Images
        self.canvas.create_image(190.0,65.0,image=self.img_rect_bar)
        self.canvas.create_image(335,220,image=self.img_playlist_bg)

        # Title Text
        self.canvas.create_text(
            36.0,
            22.0,
            anchor="nw",
            text="Below is the Currently Playing Playlist",
            fill="#C67FFC",
            font=("Montserrat Bold", 26 * -1)
        )
        self.canvas.create_text(
            36.0,
            65.0,
            anchor="nw",
            text="using this You can Choose which song to play !",
            fill="#C67FFC",
            font=("Montserrat SemiBold", 15 * -1)
        )

        # Play Button
        self.btn_play = Button(
            self,
            image=self.img_btn_play,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.parent.handle_child_btn_press(self.btn_play,"playlist_play", playlist = self.load_player_playlist()),
            relief="flat",
            bg='#FFFFFF',
            activebackground='#FFFFFF'
        )
        self.btn_play.place(
            x=255.0,
            y=355.0,
            width=141.0,
            height=39.0
        )

        # Refresh Button
        self.btn_refresh = Button(
            self,
            image=self.img_btn_refresh,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.load_player_playlist(),
            relief="flat",
            bg='#FFFFFF',
            activebackground='#FFFFFF'
        )
        self.btn_refresh.place(
            x=420.0,
            y=346.0,
            width=65.0,
            height=55.0
        )

        # Playlist
        self.playlist=Listbox(
            self,selectmode=SINGLE,bg="SlateBlue4",selectbackground='SlateBlue4',
            selectforeground="SeaGreen",fg='white',font=('Montserrat Bold',15),
            width=41,height=8,borderwidth=0,highlightthickness=0,relief="ridge")
        self.load_player_playlist()
        # load_songs_dir(self.playlist) # Fuck Around and Find Out

        self.playlist.grid(columnspan=150)
        self.playlist.place(x=50,y=110)

    def load_player_playlist(self):
        queue = self.parent.player.playlist.get_current_queue()
        self.playlist.delete(0, END)
        for song in queue:
            self.playlist.insert(END, song)
