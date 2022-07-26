
from pathlib import Path
from tkinter import *
from math import sin, cos

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)




def About(parent_window):
    canvas = Canvas(
    parent_window,
    bg = "#FFFFFF",
    height = 405,
    width = 675,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
    )
    canvas.place(x = 230, y = 72)
    canvas.create_text(
    36.0,
    43.0,
    anchor="nw",
    text="CodTubify was created by",
    fill="#C67FFC",
    font=("Montserrat Bold", 26 * -1)
    )
 
    
    global about_image_1
    about_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
    canvas.create_image(190.0,30.0,image=about_image_1)

    global about_image_2 #or this can be used : round_rectangle(180,108,510,300,fill="#171435")
    about_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
    canvas.create_image(345.0,211.0,image=about_image_2)
    
    global about_image_3
    about_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
    canvas.create_image(
    410.0,
    168.0,
    image=about_image_3
    )

    

    canvas.create_text(
    200.0,
    136.0625,
    anchor="nw",
    text="Noob",
    fill="#EFEFEF",
    font=("Montserrat SemiBold", 15 * -1)
    )

    canvas.create_text(
    200.0,
    162.0,
    anchor="nw",
    text="Arsh",
    fill="#C67FFC",
    font=("Montserrat Bold", 26 * -1)
    )

    canvas.create_text(
    197.0,
    190.0,
    anchor="nw",
    text="@iamdyeus",
    fill="#C67FFC",
    font=("Montserrat Bold", 18 * -1)
    )

    canvas.create_rectangle(
    199.0,
    219.0,
    337.0,
    221.0,
    fill="#EFEFEF",
    outline="")

    canvas.create_text(
    190.0,
    360.0,
    anchor="nw",
    text=" © 2022 Arsh, All rights reserved",
    fill="#C67FFC",
    font=("Montserrat Bold", 16 * -1)
    )

    canvas.create_text(
    180.0,
    380.0,
    anchor="nw",
    text="Open sourced under the MIT license",
    fill="#C67FFC",
    font=("Montserrat Bold", 16 * -1)
    )

    canvas.create_text(
    194.0,
    234.75,
    anchor="nw",
    text="An enthusiastic coder,  content creator, and ",
    fill="#EFEFEF",
    font=("Montserrat SemiBold", 13 * -1)
    )

    canvas.create_text(
    193.0,
    252.5625,
    anchor="nw",
    text="a student. Arsh likes to innovate new things,  ",
    fill="#EFEFEF",
    font=("Montserrat SemiBold", 13 * -1)
    )

    canvas.create_text(
    194.0,
    270.1875,
    anchor="nw",
    text="he is also very much into latest Tech.",
    fill="#EFEFEF",
    font=("Montserrat SemiBold", 13 * -1)
    )


