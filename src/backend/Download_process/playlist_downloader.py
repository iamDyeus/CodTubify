from yt_dlp import YoutubeDL

option={'final_ext': 'mp3',
 'format': 'bestaudio/best',
 'postprocessors': [{'key': 'FFmpegExtractAudio',
                     'nopostoverwrites': False,
                     'preferredcodec': 'mp3',
                     'preferredquality': '5'}],
 'outtmpl': 'src/backend/temp_audio/%(title)s.%(ext)s',
 'ffmpeg_location': 'src/backend/Download_process/ffmpeg.exe'}


def download_playlist(plylst):
    for link in plylst:
        try:
            with YoutubeDL(option) as ydl:
                ydl.download([link])
        except:
            print("Error in Downloading : " + link )
            pass



'''
Alternate Way of Downloading Playlist :  
#Didn't Worked for Me :(  

import pafy
def download_playlist(lst_of_links):
    for link in lst_of_links:
        try:
            video = pafy.new(link)
            bestaudio = video.getbestaudio(preftype="mp4")
            bestaudio.download(filepath="/temp_audio/")
            print('Downloaded: %s' % video.title)
        except Exception as e:
            print('Error in downloading Song  :',e)
            pass

download_playlist(['https://www.youtube.com/watch?v=WzQBAc8i73E','https://www.youtube.com/watch?v=BH-SnQ8J1VU','https://www.youtube.com/watch?v=Z6L4u2i97Rw'])
'''

