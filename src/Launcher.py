print("Please Use the app.py script to launch the Application\nLauncher.py script isn't Complete Yet")


#This Script Needs to be complete yet!

# what will this script do?
# 1. Starts the splash screen gui
# 2. check if the user is logged in (or if this is users first time using the app)
# 3. if not, show the login screen
# 4. if all the requirements in startup are met 
#    Run app.py script


''' 
Some EXAMPLE Code :

import subprocess
def startup():
    subprocess.Popen("python src/gui/splash_Screens/startup/gui.py",shell=True)
   
from gui.Splash_Screens.startup.gui import handling_label

try:
    startup()
    if handling_label=="Success":
        print("launching application")
        subprocess.Popen("python src/app.py",shell=True)
    elif handling_label=="Login":
        print("Login is Required")
        subprocess.Popen("python src/gui/Login_Page/gui.py",shell=True)
    elif handling_label=="Update":
        print("Update is Available")
        subprocess.Popen("python src/gui/splash_Screens/update/gui.py",shell=True)
except:
    try:
        print("Launching the App but Got some error while starting up")
        subprocess.Popen("python src/app.py",shell=True)
    except: 
        print("\nCouldn't Even start the app")
        pass
    pass
'''