#!/user/bin/env python
#  Handle creating new file

# import statements
from tkinter import filedialog
import getpass
import os
import platform
import errno

fd = filedialog


# create new file
class Newfile:

    def __init__(self, f, file):
        self.f = f
        self.file = file

    @staticmethod
    def createnewfile():

        f = fd.asksaveasfilename(defaultextension=".rpro", initialdir=defaultdirectory())
        checkcancel(f)


# open existing file
class Openfile:

    def __init__(self, f, file):
        self.f = f
        self.file = file

    @staticmethod
    def openexistingfile():

        f = fd.askopenfilename(defaultextension=".rpro", initialdir=defaultdirectory())
        checkcancel(f)


# use default working directory
def defaultdirectory():

    # get user name
    user = getpass.getuser()

    if platform.system() == 'Windows':

        initdir = 'C:/Users/%s/Documents/Rapid Pro' % user

    elif platform.system() == 'Linux':
        initdir = '/home/%s/Documents/Rapid Pro' % user

    else:
        print('Don\'t tell me you\'re running apple :S ')

    try:
        os.mkdir(initdir)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise
        return initdir


# check if action was canceled, if not, then open file
def checkcancel(var1):

    if not var1:
        print("Action canceled!")
        return None

    else:
        open(var1, 'w+')
        print(var1)
        # f.close()
