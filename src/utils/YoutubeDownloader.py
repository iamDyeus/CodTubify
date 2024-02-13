from yt_dlp import YoutubeDL
# import logging

# Configure logging
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

class MP3Downloader:
    def __init__(self,**kwargs):
        if 'options' in kwargs:
            self.options = kwargs['options']
        else:
            self.options = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'nopostoverwrites': False,
                    'preferredcodec': 'mp3',
                    'preferredquality': '320k',  # Adjust to the desired bitrate
                }],
                'outtmpl': 'media/%(title)s.%(ext)s',
                'ffmpeg_location': 'bin/ffmpeg.exe'
            }

    def set_options(self, options):
        self.options = options

    def download_mp3(self, link):
        try:
            with YoutubeDL(self.options) as ydl:
                ydl.download([link])
                # logger.info(f"Downloaded MP3 from {link}")
                return True, ydl.prepare_filename(ydl.extract_info(link, download=False))
        except Exception as e:
            # logger.error(f"Failed to download MP3 from {link}. Error: {e}")
            return False, None


'''
# Example usage:
if __name__ == "__main__":
    downloader = MP3Downloader()
    link_to_download = "https://www.youtube.com/watch?v=xLc6lwbJoxU"
    downloader.download_mp3(link_to_download)
'''