from collections import defaultdict
from pathlib import Path
from tkinter import *
from gui.Primary_Window.sub_gui.about_GUI.gui import About
from gui.Primary_Window.sub_gui.home_GUI.gui import Home
from gui.Primary_Window.sub_gui.playlist_GUI.gui import play_next,play_previous,Playlist
from gui.Primary_Window.sub_gui.featured_GUI.gui import Featured
from backend.Download_process.song_entry_identifier import is_youtube_url
from backend.Download_process.song_downloader import download_song
from backend.Download_process.playlist_scratcher import get_playlist_items
from backend.Download_process.playlist_downloader import download_playlist
from backend.Download_process.url_from_title_scraper import get_youtube_uri
from backend.Download_process.remove_temp_audio import remove_temp
from backend.player.player import *
import threading




OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./gui/Primary_Window/assets")
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)



'''def playit_button_clicked():
    user_home_entry=Home.home_entrybox.get()
    if is_youtube_url(user_home_entry):
        download_song(user_home_entry)
        play_song(user_home_entry) 
    elif user_home_entry==None:
        pass
    else:
        to_ply=get_youtube_uri(user_home_entry)
        download_song(to_ply)
        play_song(to_ply)'''

'''
def continous_playing():
    try:
        while mixer.music.get_busy()==True and pauseresume_button.config("text")[-1]=="Resume":
            continue
        else:
            if mixer.music.get_busy()==False:
                play_next() # I know the Above statement was kind of 
                            # redundant but I'm just taking extra precaution
            else: 
                pass
    except Exception as e:
        print("Got an error from continous_playing()\n",e)
        pass
    

def continous_playing_thread():
    a=threading.Thread(target=continous_playing(),daemon=True)
    a.start()
'''
##############################




initialise_mixer()


def handle_button_press(btn_name):
    global current_window
    if btn_name == "home":
        home_button_clicked()
        current_window = Home(window)
    elif btn_name == "playlist":
        playlist_button_clicked()
        current_window = Playlist(window)
    elif btn_name=="featured":
        featured_button_clicked()
        current_window = Featured(window)
    elif btn_name == "about":
        about_button_clicked()
        current_window=About(window)
    elif btn_name == "pauseresume":
        pauseresume_button_clicked()
        


# ~ FUNCTIONS FOR BUTTONS FOR CHANGING TABS ~

def home_button_clicked(): # (coordinates : x= 0 , y= 133)
    print("Home button clicked")
    canvas.itemconfig(page_navigator, text="Home")
    sidebar_navigator.place(x=0, y=133)    

def playlist_button_clicked(): # (coordinates : x= 0 , y= 184)
    print("Playlist button clicked")
    canvas.itemconfig(page_navigator, text="Playlist")
    sidebar_navigator.place(x=0, y=184)

def featured_button_clicked():
    print("Featured button clicked")
    canvas.itemconfig(page_navigator, text="Featured")
    sidebar_navigator.place(x=0, y=232)

def about_button_clicked(): # (coordinates : x= 0 , y= 232)
    print("About button clicked")
    canvas.itemconfig(page_navigator, text="About")
    sidebar_navigator.place(x=0, y=280)
    
def pauseresume_button_clicked():
    if (pauseresume_button['text']=="Pause"):
        if mixer.music.get_busy()==True:
            print("Pause button clicked")
            pause_song()
            pauseresume_button.config(image=resume_image,text="Resume")
        

    elif (pauseresume_button['text']=="Resume"):
        if mixer.music.get_busy()==False:
            print("Resume button clicked")
            resume_song()
            pauseresume_button.config(image=pause_image,text="Pause")
        

window = Tk()
window.title("CodTubify")
window.geometry("930x506")
window.configure(bg = "#171435")

'''for custom cursor'''
#cursor_path=relative_to_assets("@Busy.ani")
#window['cursor']=cursor=cursor_path

'''For Custom title bar'''
#window.overrideredirect(1)
#window.wm_attributes("-transparentcolor","#35F331")


'''For Icon'''
window.iconbitmap(relative_to_assets("icon2.ico"))


canvas = Canvas(
    window,
    bg = '#171435',
    height = 506,
    width = 930,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas.place(x = 0, y = 0)
background_image = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    566.0,
    253.0,
    image=background_image
)

current_window=Home(window)

####### HOME BUTTON #############
home_button_image = PhotoImage(
    file=relative_to_assets("button_1.png"))
home_button = Button(
    image=home_button_image,
    bg="#171435",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: handle_button_press("home"),
    relief="sunken",
    activebackground="#171435",
    activeforeground="#171435"
)
home_button.place(
    x=7.35,
    y=133.0,
    width=191.0,
    height=47.0
)
#################################

####### PLAYLIST BUTTON #############
playlist_button_image = PhotoImage(
    file=relative_to_assets("button_2.png"))
playlist_button = Button(
    image=playlist_button_image,
    borderwidth=0,
    bg="#171435",
    highlightthickness=0,
    command=lambda: handle_button_press("playlist"),
    relief="sunken",
    activebackground="#171435",
    activeforeground="#171435"
)
playlist_button.place(
    x=11.35,
    y=184.0,
    width=191,
    height=47.0
)
#####################################

####### FEATURED BUTTON #############
featured_button_image = PhotoImage(
    file=relative_to_assets("button_8.png"))
featured_button = Button(
    image=featured_button_image,
    borderwidth=0,
    bg="#171435",
    highlightthickness=0,
    command=lambda: handle_button_press("featured"),
    relief="sunken",
    activebackground="#171435",
    activeforeground="#171435"
)
featured_button.place(
    x=8.0,
    y=232.0,
    width=191.146240234375,
    height=47.0
)





####### ABOUT BUTTON ################
About_button_image = PhotoImage(
    file=relative_to_assets("button_7.png"))
About_button = Button(
    image=About_button_image,
    borderwidth=0,
    bg="#171435",
    highlightthickness=0,
    command=lambda: handle_button_press("about"),
    relief="sunken",
    activebackground="#171435",
    activeforeground="#171435"
)

About_button.place(
    x=7.351776123046875,
    y=280.0,
    width=191.146240234375,
    height=47.0
)
#####################################




######## PREVIOUS-PAUSERESUME-FORWARD BUTTONS #######

######## (i) PAUSE-RESUME BUTTON #######
pause_image = PhotoImage(
    file=relative_to_assets("button_3.png"))
resume_image = PhotoImage(
    file=relative_to_assets("button_4.png"))

global pauseresume_button
pauseresume_button = Button(
    image=pause_image,
    borderwidth=0,
    bg="#171435",
    highlightthickness=0,
    command=lambda: handle_button_press("pauseresume"),
    relief="flat",
    text=str("Pause"),
    activebackground="#171435",
    activeforeground="#171435"
)
pauseresume_button.place(
    x=90.0,
    y=421.0,
    width=40.18182373046875,
    height=40.436981201171875
)
########################################

######## (ii)  FORWARD BUTTON ##########
Forward_button_image = PhotoImage(
    file=relative_to_assets("button_5.png"))
Forward_button = Button(
    image=Forward_button_image,
    borderwidth=0,
    bg="#171435",
    highlightthickness=0,
    command=lambda: play_next(),
    relief="flat"
)
Forward_button.place(
    x=153.0,
    y=421.0,
    width=40.18182373046875,
    height=40.0
)
########################################

###### (iii)  PREVIOUS BUTTON ##########
Previous_button_image = PhotoImage(
    file=relative_to_assets("button_6.png"))
Previous_button = Button(
    image=Previous_button_image,
    borderwidth=0,
    bg="#171435",
    highlightthickness=0,
    command=lambda: play_previous(),
    relief="flat"
)
Previous_button.place(
    x=27.0,
    y=421.0,
    width=40.18182373046875,
    height=40.0
)
########################################

###################################################



##################### Navigators ###############################

####### (i)  SIDEBAR NAVIGATOR #########
sidebar_navigator = Frame(background="#FFFFFF")
sidebar_navigator.place(x=0, y=133, height=47, width=7)
########################################

####### (ii)  PAGE NAVIGATOR ###########
page_navigator = canvas.create_text(
    251.0,
    37.0,
    anchor="nw",
    text="Home",
    fill="#171435",
    font=("Montserrat Bold", 26 * -1))
########################################

#################################################################


#App name
canvas.create_text(             
    21.0,
    21.0,
    anchor="nw",
    text="CodTubify",
    fill="#FFFFFF",
    font=("Montserrat Bold", 32 * -1)
)


############## Greetings/Hello ################################ 
from gui.Primary_Window.scripts.greetings import greet
canvas.create_text(
    800.0,
    46.0,
    anchor="nw",
    text=greet(),
    fill="#808080",
    font=("Montserrat SemiBold", 16 * -1)
)
#################################################################


#Text-to-delete
canvas.create_text( #Background
    283.39056396484375,
    216.0,
    anchor="nw",
    text="(Starting the Magic",
    fill="#171435",
    font=("Montserrat Bold", 48 * -1)
)
canvas.create_text(
    311.3304748535156,
    275.0,
    anchor="nw",
    text="Loading Screens...)",
    fill="#171435",
    font=("Montserrat Bold", 48 * -1)
)


#################################################################

#window.after(1000, lambda: continous_playing_thread())

#################################################################
window.resizable(False, False)
window.mainloop()
###################################################################

