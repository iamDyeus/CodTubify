from pathlib import Path
from PIL import Image
import tkinter as tk


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)




####################################

def Loading_splash():

    root = tk.Tk()
    root.geometry("350x350")
    root.configure(bg = "#09052D")
    root.resizable(False, False)
    root.overrideredirect(1)



    # Centering the root  on the Screen
    root.withdraw()
    root.update_idletasks()  
    x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
    y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
    root.geometry("+%d+%d" % (x, y))
    root.deiconify()
    ####################################

    canvas = tk.Canvas(
        root,
        bg = "#FFFFFF",
        height = 400,
        width = 400,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)

    '''loading_gif=PhotoImage(file=relative_to_assets("loading.gif"))
    canvas.create_image(170,170,image=loading_gif)'''


    gif_label=tk.Label(image="")
    gif_label.place(x=-70,y=0)

    file=relative_to_assets("loading.gif")

    info=Image.open(file)
    frames=info.n_frames
    #print(frames)

    im = [tk.PhotoImage(file=relative_to_assets("loading.gif"), format="gif -index %i" % (i)) for i in range(frames)]

    count=0
    def animate(count):
        im2=im[count]
        gif_label.configure(image=im2)

        count +=1
        if count == frames:
            count = 0

        root.after(50, animate, count)

    while True:
        animate(count)
        root.update()
        root.mainloop()