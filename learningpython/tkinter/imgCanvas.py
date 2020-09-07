gifdir = '/home/lhj/PycharmProjects/photo/gif/'
from tkinter import *

win = Tk()
img = PhotoImage(file=gifdir + "1111.gif")
can = Canvas(win)
can.pack(fill=BOTH)
can.create_image(2, 2, image=img, anchor=NW)
win.mainloop()