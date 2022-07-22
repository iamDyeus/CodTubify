from playlist_scratcher import get_playlist_items
from playlist_downloader import download_playlist
from song_downloader import download_song
from remove_temp_audio import remove_temp
from rich import print #NO NEED OF THIS MODULE



#  Example Playlist : ("https://www.youtube.com/playlist?list=PLfP6i5T0-DkIMLNRwmJpRBs4PJvxfgwBg")
#  Example Song : ("https://www.youtube.com/watch?v=XgoxMLUjWR4")
#  Another Example Song : ("https://www.youtube.com/watch?v=4aDyjEI0KUY&list=RDMM&start_radio=1&rv=DgrjljRcgWk")




#  Asking what to Download
query=input("\n1.For Playlist ENTER '1'\n2.For Song ENTER '2'\n\n\n >>")


if query=="1":
    url=input("Enter Playlist URL >> ")
    print("\n\n\nDownloading Playlist...")
    lst=get_playlist_items(url) # Making a list of video links from playlist
    download_playlist(lst)  # Downloading each item in the list
    
elif query=="2":
    url=input("\n\nEnter Song URL >> ")
    print("\n\n\nDownloading Song...")
    download_song(url) # Downloading the song
    
else:
    print("--// Invalid Input //--")
    exit()



####### Clearing Temp Folder #######
print("\n\n\nShould we remove the Temp_Audio folder? (y/n)\n\n >>")
if input()=="y": # Removes the Temp_Audio folder after Test
    remove_temp()
else:
    exit()







