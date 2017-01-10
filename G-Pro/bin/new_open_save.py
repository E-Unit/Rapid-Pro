#!/user/bin/env python
#  Handle creating new file

# import statements
from tkinter import filedialog
import getpass
import os
import platform
import errno

fd = filedialog


class Defaultdir:

    def __init__(self, initdir, user):
        self.initdir = initdir
        self.user = user

    # test platform and make working dir if not present
    def defaultdirectory(self):

        self.initdir = None
        # get user name
        self.user = getpass.getuser()

        if platform.system() == 'Windows':

            self.initdir = 'C:/Users/%s/Documents/Rapid Pro' % self.user

        if platform.system() == 'Linux':
            self.initdir = '/home/%s/Documents/Rapid Pro' % self.user

        else:
            print('Don\'t tell me you\'re running apple :S ')

        try:
            os.mkdir(self.initdir)
        except OSError as exception:
            if exception.errno != errno.EEXIST:
                raise
            return self.initdir


class Newfile(Defaultdir):

    def __init__(self, f, file):
        self.f = f
        self.file = file

    def createnewfile(self):


        self.f = fd.asksaveasfilename(defaultextension=".rpro", initialdir=self.initdir)

        if not self.f:
            print("Action canceled!")
            return None

        else:
            self.file = open(self.f, 'w+')
            print(self.f)
            # f.close()


class Openfile(Defaultdir):

    def __init__(self, f, file):
        self.f = f
        self.file = file

    def openexistingfile(self):

        self.f = fd.askopenfilename(defaultextension=".rpro", initialdir=self.initdir)

        if not self.f:
            print("Action canceled!")
            return None

        else:
            self.file = open(self.f, 'w+')
            print(self.f)
            # f.close()
