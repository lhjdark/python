import sys
from tkinter import *


def hello(event):
    print('press twice to exit')


def quit(event):
    print("hello , I must be going")
    sys.exit()


widget = Button(None, text='hello bind world 3e')
widget.pack()
widget.bind('<Button-1>', hello)
widget.bind('<Double-1>', quit)
widget.mainloop()
