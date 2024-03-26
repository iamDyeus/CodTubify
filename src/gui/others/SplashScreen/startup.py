from pathlib import Path
import time
import threading 
from tkinter import *
import os
from tkinter.tix import STATUS


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)



# function to change display text
def startup():
    latest_version="1.0.0" #to be scraped taken from NET (probably GITHUB releases)
    version="1.0.0" #version on device

    
    global handling_label
    handling_label=None
    def handle_process():
        os.chdir("src/gui/Login_Page/assets/")
        print(os.getcwd())
        auth=open("auth.txt", "r")
        has_logedin=auth.read()
        os.chdir("../../../../")
        os.chdir("src/gui/splash_Screens/startup")
        if has_logedin=="TRUE":
            if latest_version==version:
                print("No Update Available")
                time.sleep(1)
                canvas.itemconfig(display_text, text=" Starting CodTubify...")
                time.sleep(2)
                #os.chdir("../../../../")
                #subprocess.Popen("python src/app.py", shell=True)
                print(os.getcwd())
                window.withdraw()
                print("window withdrawn...")
                handling_label=="Success"
                return handling_label
            else:
                canvas.itemconfig(display_text, text=" Updating CodTubify...")
                
		#update_software
		# once this thing starts Running Properly
		# then i can think of making something that
		# upgrades itself, until then SUFFER with me :|
                
		window.withdraw()
                handling_label=="Update"
                return handling_label

        else:
            canvas.itemconfig(display_text, text=" Starting CodTubify...")
            time.sleep(3)
            canvas.itemconfig(display_text, text="Please login to continue...", font=("Montserrat Bold", 22 * -1))
            time.sleep(3)
            window.withdraw()
            handling_label=="Login"
            return handling_label
            


    def handle_process_thread():
        a=threading.Thread(target=handle_process,daemon=True)
        a.start()

    ####################################

    window = Tk()
    window.geometry("350x350")
    window.configure(bg = "#09052D")
    window.resizable(False, False)
    window.overrideredirect(1)



    # Centering the Window  on the Screen
    window.withdraw()
    window.update_idletasks()  
    x = (window.winfo_screenwidth() - window.winfo_reqwidth()) / 2
    y = (window.winfo_screenheight() - window.winfo_reqheight()) / 2
    window.geometry("+%d+%d" % (x, y))
    window.deiconify()
    ####################################

    canvas = Canvas(
        window,
        bg = "#09052D",
        height = 350,
        width = 350,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)

    logo_img=PhotoImage(file=relative_to_assets("image_1.png"))
    canvas.create_image(170,100,image=logo_img)


    #Display Text
    display_text=canvas.create_text(
        18.0,
        223.0,
        anchor="nw",
        text="Checking For Updates...",
        fill="#FFFFFF",
        font=("Montserrat Bold", 26 * -1)
    )

    label_processes=window.after(500, handle_process_thread())
    window.mainloop()

startup()