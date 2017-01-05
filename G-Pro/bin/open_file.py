#!/user/bin/env python
#  Handle opening a file


# import statements
from tkinter import filedialog
import getpass, platform

fd = filedialog

# set default directory
def default_directory():
    #get user name
    user = getpass.getuser()

    if platform.system() == 'Windows':

        initdir = 'C:/Users/%s/Documents/Rapid Pro' % user

    if platform.system() == 'Linux':
        initdir = '/home/%s/Documents' % user

    #open_existing_file(initdir)


def open_existing_file(path):
    f = fd.askopenfilename(defaultextension=".rpro", initialdir=path)

    if not f:
        print ("Action canceled!")
        return(None)

    else:
        file = open(f, 'w+')
        print(f)
        #f.close()
