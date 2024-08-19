
# TODO : figure out if you still want win10toast module or not
# import win10toast
# toast = win10toast.ToastNotifier()
from pathlib import Path


from tkinter import  Frame , Canvas, Entry, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def home():
    Home()

class Home(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.canvas = Canvas(
            self,
            bg = "#FFFFFF",
            height = 405,
            width = 675,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        self.canvas.place(x = 0, y = 0)

        # IMAGES USED FOR HOME GUI
        self.img_entrybox = PhotoImage(file=relative_to_assets("image_1.png"))
        self.img_btn_download = PhotoImage(file=relative_to_assets("button_1.png"))

        # Song Query EntryBox
        self.entrybox_home=Entry(self)
        self.entrybox_home.place(x=90, y=202, width=495, height=40)
        self.entrybox_home.configure(font=("Montserrat Bold", 20 * -1),relief="flat",borderwidth="0",fg="#171435")
        self.canvas.create_image(341,210,image=self.img_entrybox)


        # Download Button
        self.btn_download = Button(
            self,
            image=self.img_btn_download,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.parent.handle_child_btn_press(self.btn_download,"home_download", home_entry = self.get_home_entry()),
            # self.parent.handle_child_btn_press(caller,"caller_name", **kwargs = home_entry)
            relief="flat",
            bg='#FFFFFF',
            activebackground='#FFFFFF')
        self.btn_download.place(
            x=230.0,y=310.0,width=190.0,height=48.0
        )

        self.canvas.create_text(
            90.0,
            58.0,
            anchor="nw",
            text="Download A Song Right Now!",
            fill="#C67FFC",
            font=("Montserrat Bold", 32 * -1)
        )

        self.canvas.create_text(
            130.0,
            100.0,
            anchor="nw",
            text="And Enjoy Playing it From our Playlist Tab",
            fill="#C67FFC",
            font=("Montserrat Bold", 18 * -1)
        )

    def get_home_entry(self):
        """
        Returns the content inputted in the home entry box
        """
        # give error popup if entry is empty
        inp = self.entrybox_home.get()
        if inp == "":
            print("[LOG] Entry is empty")
            return None
        # Clear the entry box
        self.entrybox_home.delete(0, 'end')
        return inp
