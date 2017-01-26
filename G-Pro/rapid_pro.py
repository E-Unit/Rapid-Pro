# !/usr/bin/python
# -*- coding: utf-8 -*-

""" rapid_pro.py
    App for programming/converting G-Code for Haas and Okuma Mills
    This app is tailored specifically for use by Rem-Tech ind.

"""


# import statements
from tkinter import Tk, Frame, Menu, Label
from PIL import Image, ImageTk
from .bin import new_open_save as nos


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


class App(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.initui()
        self.image = Image.open("rapid_pro_logo.png")
        self.img_copy = self.image.copy()
        self.background_image = ImageTk.PhotoImage(self.image)
        self.background = Label(self, image=self.background_image)
        self.background.pack(fill='both', expand='yes')
        self.background.bind('<Configure>', self._resize_image)

    def _resize_image(self, event):

        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))
        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)

    def initui(self):

        self.parent.title("Rapid Pro")
        self.pack(fill='both', expand=1)
        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)

        # filemenu = Menu(menubar)
        # recentsub = Menu(filemenu)
        filemenu = Menu(self.parent, tearoff=0)
        recentsub = Menu(filemenu, tearoff=0)

        recentsub.add_command(label="hello", command=self.dosub)

        filemenu.add_command(label="New", underline=0, command=)
        filemenu.add_command(label="Open", underline=0, command=self.dofile)
        filemenu.add_command(label="Save", underline=0, command=self.dofile)
        filemenu.add_command(label="Save As...", command=self.dofile)
        filemenu.add_separator()
        filemenu.add_command(label="Settings", underline=0, command=self.dofile)
        filemenu.add_separator()
        filemenu.add_cascade(label="Recent", menu=recentsub, underline=0)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", underline=1, command=self.onexit)
        menubar.add_cascade(label="File", menu=filemenu)

        # editMenu = Menu (menubar)
        editmenu = Menu(self.parent, tearoff=0)
        editmenu.add_command(label="Cut", command=self.doedit)
        editmenu.add_command(label="Copy", command=self.doedit)
        editmenu.add_command(label="Paste", command=self.doedit)
        editmenu.add_command(label="Select", command=self.doedit)
        editmenu.add_command(label="Select all...", command=self.doedit)
        editmenu.add_command(label="Find", command=self.doedit)
        menubar.add_cascade(label="Edit", menu=editmenu)

    @staticmethod
    def dofile():
        print("Button from file pressed")

    @staticmethod
    def doedit():
        print("Button pressed from edit")

    @staticmethod
    def onexit():
        quit()

    @staticmethod
    def dosub():
        print("Button pressed from Recent submenu")


def main():

    # Initialize main root window and center on screen
    root = Tk()
    root.state('normal')

    # Limit minimum size window can be sized to
    root.minsize(650, 450)

    # set variable for start-up screen size
    w = 700  # width of root window
    h = 500  # height of root window

    # get screen width and height
    ws = root.winfo_screenwidth()  # screen width
    hs = root.winfo_screenheight()  # screen height
    print(ws, hs)
    # calculate x and y coordinates for the root window
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root.geometry("%dx%d+%d+%d" % (w, h, x, y))
    App(root)
    root.mainloop()


if __name__ == "__main__":
    main()
