#!/user/bin/env python
#  Handle creating new file

from tkinter import filedialog

fd = filedialog

def create_new_file():
    exportFile = fd.asksaveasfile(mode='w', defaultextension=".rpro")
    print(exportFile.name)
