# gifdir = "/home/lhj/PycharmProjects/python/learningpython/tkinter/"
gifdir = '/home/lhj/PycharmProjects/photo/gif/'
from tkinter import *
win = Tk()
igm = PhotoImage(file=gifdir + "1111.gif")
Button(win, image=igm).pack()
win.mainloop()