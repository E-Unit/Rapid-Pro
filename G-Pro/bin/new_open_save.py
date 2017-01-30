#!/user/bin/env python
#  Handle creating new file

# import statements
from tkinter import filedialog
from bin import config_handler

fd = filedialog
# path = 'bin/config.ini'


# create new file
class Newfile:

    def __init__(self, f, file, path):
        self.f = f
        self.file = file
        self.path = path

    @staticmethod
    def createnewfile():
        path = 'bin/config.ini'
        f = fd.asksaveasfilename(defaultextension=".rpro", initialdir=config_handler.defaultdirectory(path))
        checkcancel(f)


# open existing file
class Openfile:

    def __init__(self, f, file, path):
        self.f = f
        self.file = file
        self.path = path

    @staticmethod
    def openexistingfile():
        path = 'bin/config.ini'
        f = fd.askopenfilename(defaultextension=".rpro", initialdir=config_handler.defaultdirectory(path))
        checkcancel(f)


# check if action was canceled, if not, then open file
def checkcancel(var1):

    if not var1:
        print("Action canceled!")
        return None

    else:
        open(var1, 'w+')
        print(var1)
        # f.close()
