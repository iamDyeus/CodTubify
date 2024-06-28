# launcher for main application

from gui.main import app
import tkinter as tk


root = tk.Tk()
root.withdraw()


if __name__ == '__main__':
    app()
    root.mainloop()

