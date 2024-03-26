"""
NIGGA,if you think you can directly run this then your completly wrong,
inorder to run this, you either run "src/laucher.py" or from some other script but from "src/" dir

see GUI import paths if you don't understand what i mean
"""


# IMPORTING PREQUISITE MODULES
from pathlib import Path
from tkinter import (
    Toplevel,
    Frame,
    Canvas,
    Button,
    PhotoImage,
    messagebox,
    StringVar,
)

# IMPORTING SUB GUI'S
from gui.Home.main import Home
from gui.Playlist.main import Playlist
# from gui.Radio.main import Radio
from gui.Featured.main import Featured
from gui.About.main import About

# DEFINING ASSET PATHS
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")
ICONS_PATH = ASSETS_PATH / Path("./icons")
IMAGES_PATH = ASSETS_PATH / Path("./images")
FONTS_PATH = ASSETS_PATH / Path("./fonts")
CURSORS_PATH = ASSETS_PATH / Path("./cursors")



def app():
    MainWindow()

class MainWindow(Toplevel):

    def __init__(self, *args, **kwargs):
        Toplevel.__init__(self, *args, **kwargs)

        # WINDOW CONFIGURATION
        self.title("CodTubify")
        self.geometry("930x506")
        self.configure(bg="#171435")
        self.resizable(False, False)
        self.iconbitmap(ICONS_PATH / Path("icon2.ico"))

        # HANDLES WINDOW CHANGES
        self.current_window = None
        self.current_window_label = StringVar()

        # WINDOW CANVAS
        self.canvas = Canvas(
            self,
            bg = '#171435',
            height = 506,
            width = 930,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        self.canvas.place(x = 0, y = 0)


        # IMAGES USED FOR TOPLEVEL GUI
        img_frames_background = PhotoImage(file = IMAGES_PATH / Path("image_1.png"))
        img_btn_home = PhotoImage(file = IMAGES_PATH / Path("button_1.png"))
        img_btn_playlist = PhotoImage(file = IMAGES_PATH / Path("button_2.png"))
        # img_btn_radio = PhotoImage(file = IMAGES_PATH / Path("button_radio.png"))
        img_btn_featured = PhotoImage(file = IMAGES_PATH / Path("button_8.png"))
        img_btn_about = PhotoImage(file = IMAGES_PATH / Path("button_7.png"))
        img_btn_pause = PhotoImage(file = IMAGES_PATH / Path("button_3.png"))
        img_btn_resume = PhotoImage(file = IMAGES_PATH / Path("button_4.png"))
        img_btn_previous = PhotoImage(file = IMAGES_PATH / Path("button_6.png"))
        img_btn_next = PhotoImage(file = IMAGES_PATH / Path("button_5.png"))

        # FRAMES BACKGROUND
        self.frames_background = self.canvas.create_image(
            566.0,
            253.0,
            image=img_frames_background,
        )

        # APP NAME
        self.name = self.canvas.create_text(             
            21.0,
            21.0,
            anchor="nw",
            text="CodTubify",
            fill="#FFFFFF",
            font=("Montserrat Bold", 32 * -1)
        )

        # RANDOM GREETING TEXT
        self.greeting = self.canvas.create_text(
            800.0,
            46.0,
            anchor="nw",
            text="HOLA!",
            fill="#808080",
            font=("Montserrat SemiBold", 16 * -1)
        )

        # SIDEBAR INDICATOR FRAME
        self.sidebar_indicator = Frame(background="#FFFFFF")
        self.sidebar_indicator.place(x=0, y=133, height=47, width=7)

        # PAGE INDICATOR TEXT
        self.page_indicator = self.canvas.create_text(
            251.0,
            37.0,
            anchor="nw",
            text="Home",
            fill="#171435",
            font=("Montserrat Bold", 26 * -1)
        ) 

        # NAVIGATION BUTTONS 
        self.btn_home = Button(
            self.canvas,
            image=img_btn_home,
            bg="#171435",
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.handle_btn_press(self.btn_home,"home"),
            cursor="hand2",
            relief="sunken",
            activebackground="#171435",
            activeforeground="#171435"
        )
        self.btn_home.place(
            x=7.35,
            y=133.0,
            width=191.0,
            height=47.0
        )

        self.btn_playlist = Button(
            self.canvas,
            image=img_btn_playlist,
            bg="#171435",
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.handle_btn_press(self.btn_playlist,"playlist"),
            cursor="hand2",
            relief="sunken",
            activebackground="#171435",
            activeforeground="#171435"
        )
        self.btn_playlist.place(
            x=11.35,
            y=184.0,
            width=191.0,
            height=47.0
        )

        self.btn_featured = Button(
            self.canvas,
            image=img_btn_featured,
            bg="#171435",
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.handle_btn_press(self.btn_featured,"featured"),
            cursor="hand2",
            relief="sunken",
            activebackground="#171435",
            activeforeground="#171435"
        )
        self.btn_featured.place(
            x=8.0,
            y=232.0,
            width=191.0,
            height=47.0
        )

        self.btn_about = Button(
            self.canvas,
            image=img_btn_about,
            bg="#171435",
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.handle_btn_press(self.btn_about,"about"),
            cursor="hand2",
            relief="sunken",
            activebackground="#171435",
            activeforeground="#171435"
        )
        self.btn_about.place(
            x=7.36,
            y=280.0,
            width=191.0,
            height=47.0
        )

        # MEDIA CONTROL BUTTONS
        self.btn_PauseResume = Button(
            self.canvas,
            image=img_btn_pause,
            bg="#171435",
            borderwidth=0,
            highlightthickness=0,
            cursor="hand2",
            relief="flat",
            text="pause",
            activebackground="#171435",
            activeforeground="#171435",
            command=lambda: self.handle_media_control(self.btn_PauseResume, self.btn_PauseResume.cget("text"))
        )
        self.btn_PauseResume.place(
            x=90.0,
            y=421.0,
            width=40.19,
            height=40.44
        )

        self.btn_Previous = Button(
            self.canvas,
            image=img_btn_previous,
            bg="#171435",
            borderwidth=0,
            highlightthickness=0,
            cursor="hand2",
            relief="flat",
            activebackground="#171435",
            activeforeground="#171435",
            command=lambda: self.handle_media_control(self.btn_Previous, "previous")
        )
        self.btn_Previous.place(
            x=27.0,
            y=421.0,
            width=40.19,
            height=40.0
        )
        
        self.btn_Next = Button(
            self.canvas,
            image=img_btn_next,
            bg="#171435",
            borderwidth=0,
            highlightthickness=0,
            cursor="hand2",
            relief="flat",
            activebackground="#171435",
            activeforeground="#171435",
            command=lambda: self.handle_media_control(self.btn_Next, "next")
        )
        self.btn_Next.place(
            x=153.0,
            y=421.0,
            width=40.18182373046875,
            height=40.0
        )


        # SCREENS LOGIC
        self.windows = {
            "home": Home(self),
            "playlist": Playlist(self),
            #"radio": Guests(self),
            "featured": Featured(self),
            "about": About(self),
        } # Loop through windows and place them

        # Set the current window to home
        self.handle_btn_press(self.btn_home, "home")
        self.sidebar_indicator.place(x=0, y=133)

        # placing it over self.frames_background
        self.current_window.place(x=230, y=72, width=675.0, height=405.0)

        self.current_window.tkraise()
        self.resizable(False, False)
        self.mainloop()


    def handle_btn_press(self, caller, name):
        # Place the sidebar on respective button
        self.sidebar_indicator.place(x=0, y=caller.winfo_y())

        # Hide all screens
        for window in self.windows.values():
            window.place_forget()

        # Set ucrrent Window
        self.current_window = self.windows.get(name)

        # Show the screen of the button pressed
        self.windows[name].place(x=215, y=72, width=1013.0, height=506.0)

        # Handle label change
        current_name = self.windows.get(name)._name.split("!")[-1].capitalize()
        self.canvas.itemconfigure(self.heading, text=current_name)

    def handle_media_control(self, caller, name):
        if name == "pause":
            caller.configure(image=self.img_btn_resume)
            caller.configure(text="resume")
        elif name == "resume":
            caller.configure(image=self.img_btn_pause)
            caller.configure(text="pause")
        elif name == "previous":
            pass
        elif name == "next":
            pass