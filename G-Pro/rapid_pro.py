#!/usr/bin/env python

""" rapid_pro.py
    App for programming/converting G-Code for Haas and Okuma Mills
    This app is taylored specifically for use by Rem-Tech ind.

"""


# import statements
import tkinter as tk
from PIL import ImageTk, Image
from bin import new_file


# ////////////////////////////////////////////
__author__ = "Ernie Peters"
__copyright__ = "Don't copy without permission"
__credits__ = "Non so far"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Ernie Peters"
__email__ = "erniepeters1@gmail.com"
__status__ = "Beta"
# ////////////////////////////////////////////


class MenuBar(tk.Menu):
    def __init__(self, parent):
        tk.Menu.__init__(self, parent)
        self.file_menu()
        self.edit_menu()
        self.help_menu()

    def file_menu(self):
        filemenu = tk.Menu(self, tearoff=False)
        self.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="New", command=new_file.create_new_file)
        filemenu.add_command(label="Open", command=self.donothingfile)
        filemenu.add_command(label="Save", command=self.donothingfile)
        filemenu.add_command(label="Save as...", command=self.donothingfile)
        filemenu.add_separator()
        filemenu.add_command(label="Settings", command=self.donothingfile)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.quit)

    def edit_menu(self):
        editmenu = tk.Menu(self, tearoff=False)
        self.add_cascade(label="Edit", menu=editmenu)
        editmenu.add_command(label="Undo", command=self.donothingedit)
        editmenu.add_command(label="Copy", command=self.donothingedit)
        editmenu.add_command(label="Cut", command=self.donothingedit)
        editmenu.add_command(label="Paste", command=self.donothingedit)

    def help_menu(self):
        helpmenu = tk.Menu(self, tearoff=False)
        self.add_cascade(label="Help", menu=helpmenu)
        helpmenu.add_command(label="About", command=self.donothinghelp)

    def donothingfile(self):
        print("Button Pressed from File Menu")

    def donothingedit(self):
        print("Button Pressed from Edit Menu")

    def donothinghelp(self):
        print("Button Pressed from Help Menu")


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        self.wm_state('zoomed')
        self.geometry("700x500")
        self.title("Rapid Pro")
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        menubar = MenuBar(self)
        self.config(menu=menubar)

if __name__ == "__main__":
    app = App()
    app.mainloop()
