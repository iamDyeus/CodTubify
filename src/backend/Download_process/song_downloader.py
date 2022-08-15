from  yt_dlp import YoutubeDL

option={'final_ext': 'mp3',
 'format': 'bestaudio/best',
 'postprocessors': [{'key': 'FFmpegExtractAudio',
                     'nopostoverwrites': False,
                     'preferredcodec': 'mp3',
                     'preferredquality': '5'}],
 'outtmpl': 'src/backend/temp_audio/%(title)s.%(ext)s',
 'ffmpeg_location': 'src/backend/Download_process/ffmpeg.exe'}

def download_song(link):
        try:
            with YoutubeDL(option) as ydl:
                ydl.download([link])
        except:
            print(Exception)
            pass

