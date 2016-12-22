#!/user/bin/env python
#  Handle creating new file

from tkinter import filedialog

fd = filedialog

def create_new_file():
    print("Hi from inside new_file")
    filename = fd.asksaveasfile(mode='w', defaultextension=".rpro")

