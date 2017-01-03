from tkinter import Tk, Frame, BOTH
import tkinter
from PIL import Image, ImageTk

class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)            
        self.parent = parent        
        self.initUI()

    def initUI(self):
        self.parent.title("PISE")
        self.pack(fill=BOTH, expand=1)

root = Tk()
root.geometry("1111x675+300+300")
app = Example(root)

im = Image.open('rapid_pro_logo.png')
tkimage = ImageTk.PhotoImage(im)
myvar=tkinter.Label(root,image = tkimage)
myvar.place(x=0, y=0, relwidth=1, relheight=1)

custName = StringVar(None)
yourName = Entry(root, textvariable=custName)
yourName.pack()

relStatus = StringVar()
relStatus.set(None)

labelText = StringVar()
labelText.set('Accuracy Level')
label1 = Label(root, textvariable=labelText, height=2)
label1.pack()

def beenClicked1():
    pass

def beenClicked5():
    pass

radio1 = Radiobutton(root, text='100%', value='1', variable = relStatus, command=beenClicked1).pack()
radio2 = Radiobutton(root, text='50%', value='5', variable = relStatus, command=beenClicked5).pack()

root.mainloop()

