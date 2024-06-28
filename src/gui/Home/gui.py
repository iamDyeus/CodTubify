
# TODO : figure out if you still want win10toast module or not
# import win10toast
# toast = win10toast.ToastNotifier()
from pathlib import Path


from tkinter import  Frame , Canvas, Entry, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def home():
    Home()

class Home(Frame):
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

        # IMAGES USED FOR HOME GUI
        self.img_entrybox = PhotoImage(file=relative_to_assets("image_1.png"))
        self.img_btn_download = PhotoImage(file=relative_to_assets("button_1.png"))

        # Song Query EntryBox
        self.entrybox_home=Entry(self)
        self.entrybox_home.place(x=90, y=202, width=495, height=40)
        self.entrybox_home.configure(font=("Montserrat Bold", 20 * -1),relief="flat",borderwidth="0",fg="#171435")
        self.canvas.create_image(341,210,image=self.img_entrybox)


        # Download Button
        self.btn_download = Button(
            self,
            image=self.img_btn_download,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.parent.handle_child_btn_press(self.btn_download,"home_download", home_entry = self.get_home_entry()),
            # self.parent.handle_child_btn_press(self.btn_home_1,"home_download", home_entry = self.get_home_entry())
            # self.parent.handle_child_btn_press(caller,"caller_name", **kwargs = home_entry)
            relief="flat",
            bg='#FFFFFF',
            activebackground='#FFFFFF').place(
                x=230.0,y=310.0,width=190.0,height=48.0
        )

        self.canvas.create_text(
            90.0,
            58.0,
            anchor="nw",
            text="Download A Song Right Now!",
            fill="#C67FFC",
            font=("Montserrat Bold", 32 * -1)
        )

        self.canvas.create_text(
            130.0,
            100.0,
            anchor="nw",
            text="And Enjoy Playing it From our Playlist Tab",
            fill="#C67FFC",
            font=("Montserrat Bold", 18 * -1)
        )

    def get_home_entry(self):
        """
        Returns the content inputted in the home entry box
        """
        # give error popup if entry is empty
        inp = self.entrybox_home.get()
        if inp == "":
            print("[LOG] Entry is empty")
            return None
        return inp


# TODO : remove the code below before pushing to main
# def download_thread(link):
#     a=threading.Thread(target=download_song(link,), daemon=True)
#     a.start()
# def Download_button_clicked(root):
#     user_home_entry=home_entrybox.get()
#     print("user asked  for :",user_home_entry)
#     if is_youtube_url(user_home_entry):
#         try:
#             toast.show_toast("Song Loading","Please Wait a Moment, while the song is being Loaded", duration=3,icon_path=relative_to_assets("codtubify.ico"))
#             #threading.Thread(target=download_song(user_home_entry,), daemon=True).start()
#             root.after(100, download_thread(user_home_entry))
#             #root.after(1000, lambda: toast.show_toast("Song Downloaded","Song Downloaded Successfully", duration=3,icon_path=relative_to_assets("codtubify.ico")))
#             #download_song(user_home_entry)
#             #Loading_splash().destroy()
#             #song_title=get_title(user_home_entry)
#             #tracks=list_tempAudio()
#             #arg=song_title,tracks
#             #threading.Thread(target=playit_song(arg,), daemon=True).run()
                  
#         except :
#             print(Exception)
            


#     elif user_home_entry=="":
#         root.after(100, lambda: toast.show_toast(" Enter Something Noob ","i won't get Dreams of what you want to download!",duration=3,icon_path=relative_to_assets("codtubify.ico")))
            
#     else:
#         video_uri=get_youtube_uri(user_home_entry)
#         toast.show_toast("Song Downloading","Please Wait a Moment, while the song is being Downloaded", duration=3,icon_path=relative_to_assets("codtubify.ico"))
#         root.after(100, download_thread(video_uri))
#         #root.after(1000, lambda: toast.show_toast("Song Downloaded","Song Downloaded Successfully", duration=3,icon_path=relative_to_assets("codtubify.ico")))
#         #toast.show_toast("Song Downloaded!","Song Downloaded Successfully!",duration=2,icon_path=relative_to_assets("codtubify.ico"))
#         #threading.Thread(target=download_song(video_uri,), daemon=True).start()
#         #song_title=(get_title(video_uri)+".mp3")
#         #tracks=list_tempAudio()
#         #ply=threading.Thread(target=play_song, args=(song_title,), daemon=True).start()


