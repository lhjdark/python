gifdir = '/home/lhj/PycharmProjects/photo/gif/'
from sys import argv
from tkinter import *
from PIL.ImageTk import PhotoImage
filename = argv[1] if len(argv) > 1 else '2222.gif'

win = Tk()
img = PhotoImage(file=gifdir + filename)
can = Canvas(win)
can.pack(fill=BOTH)
can.config(width=img.width(), height=img.height())
can.create_image(2, 2, image=img, anchor=NW)
win.mainloop()
