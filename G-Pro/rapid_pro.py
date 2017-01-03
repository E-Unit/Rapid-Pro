# !/usr/bin/python
# -*- coding: utf-8 -*-

""" rapid_pro.py
    App for programming/converting G-Code for Haas and Okuma Mills
    This app is taylored specifically for use by Rem-Tech ind.

"""


# import statements
from tkinter import Tk, Frame, Menu, Canvas, Label, PhotoImage, Image
from PIL import Image, ImageTk
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

        filemenu = Menu(menubar)
        recentsub = Menu(filemenu)
        filemenu = Menu(self.parent, tearoff=0)
        recentsub = Menu(filemenu, tearoff=0)

        recentsub.add_command(label="hello", command=self.dosub)


        filemenu.add_command(label="New", underline=0, command=new_file.create_new_file)
        filemenu.add_command(label="Open", underline=0, command=self.dofile)
        filemenu.add_command(label="Save", underline=0, command=self.dofile)
        filemenu.add_command(label="Save As...", command=self.dofile)
        filemenu.add_separator()
        filemenu.add_command(label="Settings", underline=0, command=self.dofile)
        filemenu.add_separator()
        filemenu.add_cascade(label="Recent", menu=recentsub, underline=0)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", underline=0, command=self.onexit)
        menubar.add_cascade(label="File", menu=filemenu)

        editMenu = Menu (menubar)
        editMenu = Menu(self.parent, tearoff=0)
        editMenu.add_command(label="Cut", command=self.doedit)
        editMenu.add_command(label="Copy", command=self.doedit)
        editMenu.add_command(label="Paste", command=self.doedit)
        editMenu.add_command(label="Select", command=self.doedit)
        editMenu.add_command(label="Select all...", command=self.doedit)
        editMenu.add_command(label="Find", command=self.doedit)
        menubar.add_cascade(label="Edit", menu=editMenu)

    def dofile(self):
        print ("Button from file pressed")

    def doedit(self):
        print("Button pressed from edit")

    def onexit(self):
        self.quit()

    def dosub(self):
        print ("Button pressed from Recent submenu")


def main():

    root = Tk()
    root.state('normal')
    root.geometry("700x500")
    mainGUI = App(root)
    root.mainloop()


if __name__ == "__main__":
    main()
