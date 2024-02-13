from mediaCollector.YoutubeCollector import YoutubeCollector 

if __name__ == '__main__':
    collector = YoutubeCollector()
    link_to_download = "https://www.youtube.com/watch?v=xLc6lwbJoxU"
    collector.collect(link_to_download)

    title = "Desi kalakaar"
    collector.collect(title)
