import pygame.mixer as mixer
import os


def initialise_mixer():
    mixer.init()



def play_song(sound):
    #check_for_directory()
    mixer.music.load(sound)
    mixer.music.play()
    #return_to_main_directory()


def make_playlist():
    check_for_directory()
    song_list=[]
    tracks = os.listdir()
    for track in tracks:
        song_list.append(track)
    return_to_main_directory()
    return song_list


def list_tempAudio():
    check_for_directory()
    lst=os.listdir()
    return_to_main_directory()
    return lst

def list_tempAudio_nondir():
    lst=os.listdir()
    return lst

def index_of_song(song,lst):
    for i in range(len(lst)):
        if song==lst[i]:
            return i-1
    return i-1


def pause_song():
    mixer.music.pause()


def resume_song():
    mixer.music.unpause()


def stop_song():
    mixer.music.stop()

#### Playing with the Directorys ########################################
# Without These Two Functions, the entire application would be Fk'ed up

def check_for_directory():
    #print("\nBefore check_for_directory Used: ",os.getcwd())                                               
    if os.getcwd()==("src/backend/temp_audio"):
        pass
    else: os.chdir("src/backend/temp_audio")    
    #print("\nAfter check_for_directory: ",os.getcwd())


def return_to_main_directory():
    #For a More detailed Understanding uncomment these print statements
    #print("\nBefore return_to_main_directory: ",os.getcwd())
    os.chdir("../../../") 
    #print("\nAfter return_to_main_directory: ",os.getcwd())


def return_to_main_directory_from_playlist():
    #Had to make this Function as os.chdir("../../../")  wasn't going back to the Desired Dir
    #For a More detailed Understanding uncomment the print statements
    #print(" before return_to_main_directory: ",os.getcwd())
    os.chdir("../../../../") 
    #print("after return_to_main_directory: ",os.getcwd())

#############################################################










