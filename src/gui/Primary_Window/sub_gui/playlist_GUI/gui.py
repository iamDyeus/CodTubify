from pathlib import Path
import threading
from tkinter import *
from xml.dom import IndexSizeErr
from backend.player.player import *

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


    

def play_next():
    global currsong
    print("play next")
    try:
        check_for_directory()
        currsong=playlist.get(ACTIVE)
        indx=index_of_song(currsong,tracks)
        
        next_song=tracks[indx+1]
        playlist.selection_clear(0,END)
        playlist.selection_set(indx+1)
        playlist.activate(index=indx+1)
        mixer.music.load(next_song)
        mixer.music.play()
        return_to_main_directory()
    except:
        playlist.selection_clear(0,END)
        playlist.selection_set(indx+1)
        playlist.activate(index=indx+1)
        print("error from play_next()\n",Exception)
        return_to_main_directory()



# When Using the Current method below, for automatically playing the
# next song in the playlist, it just fk's up the Mixer.
# Therefore i would look at it later
# i got Error from  :  "while mixer.music.get_busy()==True:"
# this even trys to plays the next song when mixer is paused.
'''
def continous_playing():
    try:
        while mixer.music.get_busy()==True : # Solution : and pauseresume_button.config("text")[-1]=="Pause":
            continue
        else:
            if pauseresume_button.config('text')[-1]=='Pause':
                play_next()
            else: 
                pass
    except Exception as e:
        print("Got an error from continous_playing()\n",e)
        pass
    

def continous_playing_thread():
    a=threading.Thread(target=continous_playing(),daemon=True)
    a.start()
'''

def play_continous(lst_itm):
    try:
        while mixer.music.get_busy()==True :
            continue
        else:
            currsong=playlist.get(ACTIVE)
            indx=index_of_song(currsong,tracks)
            next_song=tracks[indx+1]
            mixer.Channel.queue(next_song)
    except:
        print("error in play_continous()")
        pass

def play_continous_thread(lst_itm):
    a=threading.Thread(target=play_continous,args=(lst_itm),daemon=True)
    a.start()


def play_previous():
    check_for_directory()
    try:
        currsong=playlist.get(ACTIVE)
        indx=index_of_song(currsong,tracks)
        prv_song=tracks[indx-1]
        playlist.selection_clear(0,END)
        playlist.selection_set(indx-1)
        playlist.activate(index=indx-1)
        try:
            mixer.music.load(prv_song)
            mixer.music.play()
        except Exception as e: 
            print("error in playing from play_previous.mixer :\n",e)
            pass
        print("previous song played :)")
        return_to_main_directory()
    except:
        playlist.selection_clear(0,END)
        playlist.selection_set(indx+1)
        playlist.activate(index=indx+1)
        print("Got Error in play_previous() :\n",Exception)
        return_to_main_directory()





def playlist_play_button_clicked(root):
    print("playlist play button clicked")
    check_for_directory()
    for currentsong in playlist.curselection():
        currentsong=playlist.get(ACTIVE)
        print(currentsong)
        try:
            mixer.music.load(currentsong)
            mixer.music.play()
        except:
            print("error ",Exception)
            pass
    return_to_main_directory()
    #root.after(1000,play_continous_thread(playlist))    


def song_seprator(obj,lst):
    for i in lst:
        if i.endswith(".mp3"):
            obj.insert(END,i)
    
def song_seprator_thread(obj,lst):
    a=threading.Thread(target=song_seprator,args=(obj,lst),daemon=True)
    a.start()






def Playlist(parent):
    canvas = Canvas(
    parent,
    bg = "#FFFFFF",
    height = 405,
    width = 675,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")


    
    canvas.place(x = 230, y = 72)
    
    global playlist_bar_image
    playlist_bar_image = PhotoImage(file=relative_to_assets("image_2.png"))
    canvas.create_image(190.0,65.0,image=playlist_bar_image)

    canvas.create_text(
        36.0,
        22.0,
        anchor="nw",
        text="Below is the Currently Playing Playlist",
        fill="#C67FFC",
        font=("Montserrat Bold", 26 * -1)
    )

    
    global playlist_background_image
    playlist_background_image = PhotoImage(file=relative_to_assets("image_1.png"))
    canvas.create_image(335,220,image=playlist_background_image)



    canvas.create_text(
        36.0,
        65.0,
        anchor="nw",
        text="using this You can Choose which song to play !",
        fill="#C67FFC",
        font=("Montserrat SemiBold", 15 * -1)
    )

    global playlist_button_image_1
    playlist_button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    Button(
        image=playlist_button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: threading.Thread(target=playlist_play_button_clicked,args= (parent,), daemon=True).start(),
        relief="flat",
        bg='#FFFFFF',
        activebackground='#FFFFFF'
    ).place(
        x=485.0,
        y=425.0,
        width=141.0,
        height=39.0
    )



    #################### Playlist #################################################################################################################
    global playlist
    playlist=Listbox(parent,selectmode=SINGLE,bg="SlateBlue4",selectbackground='SlateBlue4',selectforeground="SeaGreen",fg='white',font=('Montserrat Bold',15),width=41,height=8,borderwidth=0,highlightthickness=0,relief="ridge")
    playlist.grid(columnspan=150)
    playlist.place(x=276,y=182)
 
    ################################################################################################################################################

    #### Listing Dir and Songs #####################################################################################################################

    global tracks
    tracks=list_tempAudio()
    parent.after(100,lambda:song_seprator_thread(playlist,tracks))
    ################################################################################################################################################


