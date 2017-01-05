#!/user/bin/env python
#  Handle creating new file

from tkinter import filedialog
from bin import default_dir.de

fd = filedialog
df = default_dir.defaultDir


class newFile():

    def __init__(self, parent):
        self.parent=parent


    def create_new_file(path):

        df.default_directory(path)

        f = fd.asksaveasfilename(defaultextension=".rpro", initialdir=path)

        if not f:
            print ("Action canceled!")
            return(None)

        else:
            file = open(f, 'w+')
            print(f)
            #f.close()

