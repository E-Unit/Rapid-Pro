#!/user/bin/env python
#  Handle creating new file

from tkinter import filedialog
import platform, getpass, os, errno


fd = filedialog


def default_directory():
    #get user name
    user = getpass.getuser()

    if platform.system() == 'Windows':

        initdir = 'C:/Users/%s/Documents/Rapid Pro' % user

    if platform.system() == 'Linux':
        initdir = '/Home/%s/Documents' % user

    try:
        os.mkdir(initdir)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

    create_new_file(initdir)


def create_new_file(path):
    f = fd.asksaveasfilename(defaultextension=".rpro", initialdir=path)

    if not f:
        print ("Action canceled!")
        return(None)

    else:
        file = open(f, 'w+')
        print(f)
        #f.close()

