import os
from yt_dlp import YoutubeDL

class MP3Downloader:
    def __init__(self, **kwargs):
        media_dir = os.path.abspath('media/')
        if 'options' in kwargs:
            self.options = kwargs['options']
        else:
            self.options = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'nopostoverwrites': False,
                    'preferredcodec': 'mp3',
                    'preferredquality': '320k',
                }],
                'outtmpl': os.path.join(media_dir, '%(title)s.%(ext)s'),
                'ffmpeg_location': os.path.abspath('bin/ffmpeg.exe')
            }

    def set_options(self, options):
        self.options = options

    def download_mp3(self, link):
        try:
            with YoutubeDL(self.options) as ydl:
                result = ydl.download([link])
                if result == 0:  # 0 indicates success
                    file_path = ydl.prepare_filename(ydl.extract_info(link, download=False))
                    file_name = os.path.basename(file_path)
                    base, ext = os.path.splitext(file_name)
                    mp3_file_name = f"{base}.mp3"

                    return True, mp3_file_name
                else:
                    return False, None
        except Exception as e:
            print(f"Failed to download MP3 from {link}. Error: {e}")
            return False, None


'''
# Example usage:
if __name__ == "__main__":
    downloader = MP3Downloader()
    link_to_download = "https://www.youtube.com/watch?v=xLc6lwbJoxU"
    downloader.download_mp3(link_to_download)
'''