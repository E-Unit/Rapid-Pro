#!/user/bin/env python
#  Handle creating new file

from tkinter import filedialog
import getpass, os


fd = filedialog


class Newfile():

    def createNewFile():

        path = Defaultdir()

        f = fd.asksaveasfilename(defaultextension=".rpro", initialdir=path)

        if not f:
            print ("Action canceled!")
            return(None)

        else:
            file = open(f, 'w+')
            print(f)
            #f.close()

class Openfile():

    def openExistingFile(self):

        f = fd.askopenfilename(defaultextension=".rpro", initialdir=self.path)

        if not f:
           print ("Action canceled!")
           return(None)

        else:
            file = open(f, 'w+')
            print(f)
            #f.close()


class Defaultdir:

    initdir = None

    #test platform and make working dir if not present
    def defaultDirectory(self):

        self.initdir = initdir

        #get user name
        user = getpass.getuser()

        if platform.system() == 'Windows':

            initdir = 'C:/Users/%s/Documents/Rapid Pro' % user

        if platform.system() == 'Linux':
            initdir = '/home/%s/Documents/Rapid Pro' % user

        else:
            print("What in the world is your Operating System!?")

        try:
            os.mkdir(initdir)
        except OSError as exception:
            if exception.errno != errno.EEXIST:
                raise
            return(initdir)
