
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/open-source.svg)](https://forthebadge.com)

![starts](https://badgen.net/github/stars/iamDyeus/CodTubify)
![issues](https://badgen.net/github/issues/iamDyeus/CodTubify)
![forks](https://badgen.net/github/forks/iamDyeus/CodTubify)
![license](https://badgen.net/github/license/iamDyeus/CodTubify)


<img height="300" width="300" alt="codtubify" src="https://user-images.githubusercontent.com/87000693/181087300-2e235f00-e661-4fd8-be34-35f14bda1a8e.png">

# About CodTubify 🎵 - An Online Music Player 
CodTubify is a Music Player project, fully developed in Python. It can Play your favorite Songs or any Youtube Playlist without any interruption.

<br />
<br />


## Requirements
* Operation system: **Windows**
* Python Version: **3.9.x**
### Required Modules
* Refer to [`requirements.txt`](src/requirements.txt)
* Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all the Required Modules.
```bash
python -m pip install -r requirements.txt
```
### Required Audio PostProcessors 
* [FFMPEG AND FFPROBE](https://bit.ly/ffmpeg_ffprobe_exe)
( just download the EXE's from the given link and extract them in "src/backend/Download_process/" before starting the application) 
* Or refer to [`IMPORTANT.md`](src/backend/Download_process/important.md)


<br />
<br />


## The Purpose
The purpose of this project really was to create an application that used a song-name/title or any Youtube URL as an input and downloads a MP3 copy of the desired user input, it then works as a Normal Audio player and basically plays the downloaded Audio, contrary to popular belief of streaming Music instead.

### Technologies
- Python (basically to create everything init)
- Audio PostProcessors (Audio files conversions)
- GitHub (Proejct and Issues)

### Significant Changes
This project required me to utilize many different aspects of what I learned so far in the last 2 Months. I incorporated Modules like yt-dlp and pygame to assist in Downloading Audio Files and Playing them respectively. Instead of traditional Object-oriented way of Programming in tkinter (using CLASSES etc) , i tried to make things as simple as Possible.

### Challenges
- There were significant challenges on this project that had a lot to do with traversing the unknown. Firstly, after i decided NOT to use the Object-oriented Programming approach for the GUI. For a while i was left Confused, because it was not one single gui i was working with, it was a group of many Nested GUI's combined together. though after waiting for someone to answer my questions on stackoverflow (which no one did to this date). I started figuring it out in my Way, Hopefully i was Able to Link all the GUI's with each other. (probably after creating a lot of mess in the code)
- Once i completed the GUI, the second problem which i was encountering was that the audio file downloaded using yt-dlp wasn't really an audio file, so i had to Convert the Downloaded File into a .mp3 using PostProcessors Such as : *FFMPEG/FFPROBE* , so that they become playable with pygame.
- Also if i start listing all the challenges i faced while making it, then probably i would write an entire Nowel here so i'll just keep it short.  

### Things To Consider
I strongly suggest to use VScode or Pycharm or any other Code editor for running the app.py script because i have messed up very much in Directory's and stuff.
(if you DIDN'T understand what i mean :"JUST OPEN THE REPO's FOLDER USING A CODE EDITOR AND THEN RUN THE app.py script ") 

<br />
<br />


## APP PREVIEW
<table>
    <tr>
        <td>
            <img src="https://user-images.githubusercontent.com/87000693/181092881-99f287c9-382d-40b4-97e4-0d02d3d3cfc7.png" />
            <br />
            <p align="center">Home Tab</p></td>
        <td>
            <img src="https://user-images.githubusercontent.com/87000693/181092889-bd8016ee-d09e-4e91-b3c5-c0db5ca14526.png" />
            <br />
            <p align="center">Playlist Tab</p></td>
    </tr>
    <tr>
        <td>
            <img src="https://user-images.githubusercontent.com/87000693/181092894-603f8288-1966-4c08-8476-d3e138285046.png" />
            <br />
            <p align="center">Featured Tab</p></td>
        <td>
            <img src="https://user-images.githubusercontent.com/87000693/181092901-ea965dad-7c3f-4f6e-8266-828f7623a363.png" />
            <br />
            <p align="center">About Page</p></td>
    </tr>
    <tr>
        <td>
            <img src="https://user-images.githubusercontent.com/87000693/181095614-778db235-bcec-4d7a-963a-250a0740ba92.png" />
            <br />
            <p align="center">Login GUI</p></td>
    </tr>
</table>


<br />
<br />



# License

Distributed under the MIT License. See [`LICENSE.txt`](/LICENSE.txt) for more information.

<br />


### CONTRIBUTING
* Pull Requests (PRs) are welcome :relaxed:
* For major changes, please discuss on discussions about what you would like to change.
* Try to add useful comments
* Please make sure to update tests as appropriate.
* If you have a suggestion that would make this better, please fork the repo and create a pull request. 
  You can also simply open an issue with the tag "enhancement". Don't forget to give the project a star! Thanks again!

# Acknowledgments

-   **Parth Jadhav and team** for their Amazing [`Tkinter Designer`](https://github.com/ParthJadhav/Tkinter-Designer).
-   **Mohit & Anirudh** for there awesome project [`HotinGo`](https://github.com/Just-Moh-it/HotinGo) as the inpiration for GUI.
-   [**Canva**](https://www.canva.com) for making the Graphic Design Process Much Easier For me.
-   [`yt-dlp`](https://discord.com/invite/FumpHSsjep) and [`pygame`](https://discord.com/invite/EaWkr5TVQy) Discord Mods/Helpers for Helping me in most of my Noob queries.

<br/>


<img  src="https://madewithlove.now.sh/in?heart=true&colorA=%23ff9933&colorB=%23138808&template=for-the-badge" alt="Made with love in India">
