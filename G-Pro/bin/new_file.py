#!/user/bin/env python
#  Handle creating new file

from tkinter import filedialog
import os, os.path

fd = filedialog

def create_new_file():
    exportFile = fd.asksaveasfile(mode='w', defaultextension=".rpro")
    print(exportFile)
    # test if file created successfully
    if os.path.isfile('exportFile')==True:
        print("File was created successfully")

