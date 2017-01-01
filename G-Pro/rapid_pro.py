# !/usr/bin/python
# -*- coding: utf-8 -*-

""" rapid_pro.py
    App for programming/converting G-Code for Haas and Okuma Mills
    This app is taylored specifically for use by Rem-Tech ind.

"""


# import statements
from tkinter import Tk, Frame, Menu
from PIL import ImageTk, Image
# from bin import new_file


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
        self.initUI()


    def initUI(self):

        self.parent.title("Rapid Pro")

        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)



        fileMenu = Menu(menubar)
        submenu = Menu(fileMenu)
        fileMenu = Menu(self.parent, tearoff=0)
        submenu = Menu(fileMenu, tearoff=0)
        submenu.add_command(label="hello", command=self.doSub)
        fileMenu.add_command(label="New", underline=0, command=self.doFile)
        fileMenu.add_command(label="Open", underline=0, command=self.doFile)
        fileMenu.add_command(label="Save", underline=0, command=self.doFile)
        fileMenu.add_command(label="Save As...", command=self.doFile)
        fileMenu.add_separator()
        fileMenu.add_command(label="Settings", underline=0, command=self.doFile)
        fileMenu.add_separator()
        fileMenu.add_cascade(label="Recent", menu=submenu, underline=0)
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", underline=0, command=self.onExit)
        menubar.add_cascade(label="File", menu=fileMenu)

        editMenu = Menu (menubar)
        editMenu = Menu(self.parent, tearoff=0)
        editMenu.add_command(label="Cut", command=self.doEdit)
        editMenu.add_command(label="Copy", command=self.doEdit)
        editMenu.add_command(label="Paste", command=self.doEdit)
        editMenu.add_command(label="Select", command=self.doEdit)
        editMenu.add_command(label="Select all...", command=self.doEdit)
        editMenu.add_command(label="Find", command=self.doEdit)
        menubar.add_cascade(label="Edit", menu=editMenu)

    def doFile(self):
        print ("Button from file pressed")

    def doEdit(self):
        print("Button pressed from edit")

    def onExit(self):
        self.quit()

    def doSub(self):
        print ("Button pressed from Recent submenu")


def main():

    root = Tk()
    root.geometry("700x500")
    mainGUI = App(root)
    root.mainloop()


if __name__ == "__main__":
    main()
