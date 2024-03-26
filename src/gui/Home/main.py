from backend.Download_process.song_entry_identifier import is_youtube_url
from backend.Download_process.song_downloader import download_song
from backend.Download_process.url_from_title_scraper import get_youtube_uri
import win10toast
toast = win10toast.ToastNotifier()
from pathlib import Path
import threading


from tkinter import  Canvas, Entry, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def download_thread(link):
    a=threading.Thread(target=download_song(link,), daemon=True)
    a.start()
    


def Download_button_clicked(root):
    user_home_entry=home_entrybox.get()
    print("user asked  for :",user_home_entry)
    if is_youtube_url(user_home_entry):
        try:
            toast.show_toast("Song Loading","Please Wait a Moment, while the song is being Loaded", duration=3,icon_path=relative_to_assets("codtubify.ico"))
            #threading.Thread(target=download_song(user_home_entry,), daemon=True).start()
            root.after(100, download_thread(user_home_entry))
            #root.after(1000, lambda: toast.show_toast("Song Downloaded","Song Downloaded Successfully", duration=3,icon_path=relative_to_assets("codtubify.ico")))
            #download_song(user_home_entry)
            #Loading_splash().destroy()
            #song_title=get_title(user_home_entry)
            #tracks=list_tempAudio()
            #arg=song_title,tracks
            #threading.Thread(target=playit_song(arg,), daemon=True).run()
                  
        except :
            print(Exception)
            


    elif user_home_entry=="":
        root.after(100, lambda: toast.show_toast(" Enter Something Noob ","i won't get Dreams of what you want to download!",duration=3,icon_path=relative_to_assets("codtubify.ico")))
            
    else:
        video_uri=get_youtube_uri(user_home_entry)
        toast.show_toast("Song Downloading","Please Wait a Moment, while the song is being Downloaded", duration=3,icon_path=relative_to_assets("codtubify.ico"))
        root.after(100, download_thread(video_uri))
        #root.after(1000, lambda: toast.show_toast("Song Downloaded","Song Downloaded Successfully", duration=3,icon_path=relative_to_assets("codtubify.ico")))
        #toast.show_toast("Song Downloaded!","Song Downloaded Successfully!",duration=2,icon_path=relative_to_assets("codtubify.ico"))
        #threading.Thread(target=download_song(video_uri,), daemon=True).start()
        #song_title=(get_title(video_uri)+".mp3")
        #tracks=list_tempAudio()
        #ply=threading.Thread(target=play_song, args=(song_title,), daemon=True).start()
        
            


def Home(parent):
    canvas = Canvas(
        parent,
        bg = "#FFFFFF",
        height = 405,
        width = 675,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 230, y = 72)

    global home_entrybox
    home_entrybox=Entry()
    home_entrybox.place(x=320, y=275, width=500, height=40)
    home_entrybox.configure(font=("Montserrat Bold", 20 * -1),relief="flat",borderwidth="0",fg="#171435")

    global entrybox_image
    entrybox_image = PhotoImage(file=relative_to_assets("image_1.png"))
    canvas.create_image(341,210,image=entrybox_image)


    global home_button_image_1
    home_button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    Button(
        image=home_button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: threading.Thread(target=Download_button_clicked,args=(parent,),daemon=True).start(),
        relief="flat",
        bg='#FFFFFF',
        activebackground='#FFFFFF').place(
            x=460.0,y=390.0,width=190.0,height=48.0)


    canvas.create_text(
        90.0,
        58.0,
        anchor="nw",
        text="Download A Song Right Now!",
        fill="#C67FFC",
        font=("Montserrat Bold", 32 * -1)
    )
    canvas.create_text(
        130.0,
        100.0,
        anchor="nw",
        text="And Enjoy Playing it From our Playlist Tab",
        fill="#C67FFC",
        font=("Montserrat Bold", 18 * -1)
    )
