
from pathlib import Path
from tkinter import *
from math import sin, cos

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def about():
    About()

class About(Frame):
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


        # IMAGES USED FOR FEATURED GUI
        self.about_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
        self.about_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
        self.about_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
        
        
        self.canvas.create_text(
            36.0,
            43.0,
            anchor="nw",
            text="CodTubify was created by",
            fill="#C67FFC",
            font=("Montserrat Bold", 26 * -1)
        )
    
        
        
        self.canvas.create_image(190.0,30.0,image=self.about_image_1)
        self.canvas.create_image(345.0,211.0,image=self.about_image_2)
        

        self.canvas.create_image(
        410.0,
        168.0,
        image=self.about_image_3
        )

        self.canvas.create_text(
        200.0,
        136.0625,
        anchor="nw",
        text="Noob",
        fill="#EFEFEF",
        font=("Montserrat SemiBold", 15 * -1)
        )

        self.canvas.create_text(
        200.0,
        162.0,
        anchor="nw",
        text="Arsh",
        fill="#C67FFC",
        font=("Montserrat Bold", 26 * -1)
        )
        
        self.canvas.create_text(
        197.0,
        190.0,
        anchor="nw",
        text="@iamdyeus",
        fill="#C67FFC",
        font=("Montserrat Bold", 18 * -1)
        )

        self.canvas.create_rectangle(
        199.0,
        219.0,
        337.0,
        221.0,
        fill="#EFEFEF",
        outline="")

        self.canvas.create_text(
        190.0,
        360.0,
        anchor="nw",
        text=" © 2022 Arsh, All rights reserved",
        fill="#C67FFC",
        font=("Montserrat Bold", 16 * -1)
        )

        self.canvas.create_text(
        180.0,
        380.0,
        anchor="nw",
        text="Open sourced under the MIT license",
        fill="#C67FFC",
        font=("Montserrat Bold", 16 * -1)
        )

        self.canvas.create_text(
        194.0,
        234.75,
        anchor="nw",
        text="An enthusiastic coder,  content creator, and ",
        fill="#EFEFEF",
        font=("Montserrat SemiBold", 13 * -1)
        )

        self.canvas.create_text(
        193.0,
        252.5625,
        anchor="nw",
        text="a student. Arsh likes to innovate new things,  ",
        fill="#EFEFEF",
        font=("Montserrat SemiBold", 13 * -1)
        )

        self.canvas.create_text(
        194.0,
        270.1875,
        anchor="nw",
        text="he is also very much into latest Tech.",
        fill="#EFEFEF",
        font=("Montserrat SemiBold", 13 * -1)
        )



