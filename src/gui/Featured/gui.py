from pathlib import Path

from win10toast import ToastNotifier
# from backend.Download_process.playlist_scratcher import get_playlist_items
# from backend.Download_process.playlist_downloader import download_playlist
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox, Frame
import threading

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


# def download_process(playlist_url):
#     playlist_items = get_playlist_items(playlist_url)
#     download_playlist(playlist_items)
#     print("Downloaded Playlist")

# def download_thread(link):
#     a=threading.Thread(target=download_process(link,), daemon=True)
#     a.start()


# def handle_button_press(btn_name, root):
#     if btn_name=="coding":
#         ToastNotifier().show_toast("Downloading","Please Don't Click on any other playlist Button while this playlist is downloading", duration=3,icon_path=relative_to_assets("codtubify.ico"))
#         root.after(100,download_thread("https://www.youtube.com/playlist?list=PLIut9bR_W7KXYMofJrzerpWSrPp6za34B"))
        
#     elif btn_name=="lofi":
#         root.after(100,download_thread("https://www.youtube.com/playlist?list=PLfP6i5T0-DkIMLNRwmJpRBs4PJvxfgwBg"))
#         ToastNotifier().show_toast("Downloading","Please Don't Click on any other playlist Button while this playlist is downloading", duration=3,icon_path=relative_to_assets("codtubify.ico"))
        
#     elif btn_name=="bass":
#         ToastNotifier().show_toast("Downloading","Please Don't Click on any other playlist Button while this playlist is downloading", duration=3,icon_path=relative_to_assets("codtubify.ico"))
#         root.after(100,download_thread("https://www.youtube.com/playlist?list=PL6vFaUSqVjRnYH6iULv1WzcK4V0d-S1t-"))
        
#     else:
#         print("Other Playlist is already downloading!\nDo you Want to kill you Damn Device?")


# def featured_add_playlist_button_clicked():
#     print("Featured Tab's Add to playlist button clicked")
#     print("Feature Not Available Yet!\nDev is too Lazy to work on it :(")
#     messagebox.showwarning("Feature Not Available ", "😓\nDev is too Lazy to work on it :(")


def featured():
    Featured()

class Featured(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.canvas = Canvas(
            self,
            bg = "#FFFFFF",
            height = 405,
            width = 675,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        self.canvas.place(x = 0, y = 0)


        # IMAGES USED FOR FEATURED GUI
        self.img_featured_coding_btn = PhotoImage(file=relative_to_assets("image_coding.png"))
        self.img_featured_lofi_btn = PhotoImage(file=relative_to_assets("image_lofi.png"))
        self.img_featured_add_btn = PhotoImage(file=relative_to_assets("image_2.png"))
        self.img_featured_bass_btn = PhotoImage(file=relative_to_assets("image_bass.png"))
        self.img_playlist_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))


        # Coding Playlist
        self.btn_coding = Button(self,
            image=self.img_featured_coding_btn,
            borderwidth=0,
            highlightthickness=0,
            # command=lambda: threading.Thread(target=handle_button_press,args=("coding",parent),daemon=True).start(),
            command=lambda: print("Coding Playlist Button Clicked"),
            relief="flat",
            activebackground="#FFFFFF",
            activeforeground="#FFFFFF"
        )
        self.btn_coding.place(x=55, y=70, width=117, height=112)




        # Lofi Playlist
        self.btn_lofi = Button(self,
            image=self.img_featured_lofi_btn,
            borderwidth=0,
            highlightthickness=0,
            # command=lambda: threading.Thread(target=handle_button_press,args=("lofi",parent),daemon=True).start(),
            command=lambda: print("Lofi Playlist Button Clicked"),
            relief="flat",
            activebackground="#FFFFFF",
            activeforeground="#FFFFFF"
        )
        self.btn_lofi.place(x=230, y=70, width=117, height=112)


        # Bass Playlist
        self.btn_bass = Button(self,
            image=self.img_featured_bass_btn,
            borderwidth=0,
            highlightthickness=0,
            # command=lambda: threading.Thread(target=handle_button_press, args=("bass",parent),daemon=True).start(),
            command=lambda: print("Bass Playlist Button Clicked"),
            relief="flat",
            activebackground="#FFFFFF",
            activeforeground="#FFFFFF"
        )
        self.btn_bass.place(x=405, y=70, width=117, height=112)

        

        #Add playlist
        self.btn_add_playlist = Button(self,
            image=self.img_featured_add_btn,
            borderwidth=0,
            highlightthickness=0,
            # command=lambda: featured_add_playlist_button_clicked(),
            command=lambda: print("Add Playlist Button Clicked"),
            relief="flat",
            activebackground="#FFFFFF",
            activeforeground="#FFFFFF"
        )
        self.btn_add_playlist.place(x=55, y=260, width=117, height=112)

        


        #Playlist 1
        self.round_rectangle(237,266,349,375,fill="#171435",outline="")
        self.canvas.create_text(259,305,
            anchor="nw",
            text="Playlist 1",
            fill="#C67FFC",
            font=("Montserrat Bold", 15 * -1)
        )

        #Playlist 2
        self.round_rectangle(413,266,531,375,fill="#171435",outline="")
        self.canvas.create_text(434,305,
            anchor="nw",
            text="Playlist 2",
            fill="#C67FFC",
            font=("Montserrat Bold", 15 * -1)
        )


        self.canvas.create_text(
            52.0,
            212.0,
            anchor="nw",
            text="Your Playlists :",
            fill="#C67FFC",
            font=("Montserrat Bold", 32 * -1)
        )


        self.canvas.create_image(
            342.0,
            201.99993896484375,
            image=self.img_playlist_image_1
        )

        self.canvas.create_text(
            52.0,
            21.0,
            anchor="nw",
            text="Our Playlists :",
            fill="#C67FFC",
            font=("Montserrat Bold", 32 * -1)
        )


    def round_rectangle(self,x1, y1, x2, y2, radius=25 , **kwargs):
        points = [x1+radius, y1,
                x1+radius, y1,
                x2-radius, y1,
                x2-radius, y1,
                x2, y1,
                x2, y1+radius,
                x2, y1+radius,
                x2, y2-radius,
                x2, y2-radius,
                x2, y2,
                x2-radius, y2,
                x2-radius, y2,
                x1+radius, y2,
                x1+radius, y2,
                x1, y2,
                x1, y2-radius,
                x1, y2-radius,
                x1, y1+radius,
                x1, y1+radius,
                x1, y1]
        return self.canvas.create_polygon(points, **kwargs, smooth=True)
    
