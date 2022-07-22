import os

def remove_temp():
    os.chdir('src/backend/temp_audio/')
    tracks = os.listdir()
    for track in tracks:
        os.remove(track)
    os.chdir('../../../')
    os.rmdir('src/backend/temp_audio')
    print("Removed temp_audio folder")



