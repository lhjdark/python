from tkinter import *


def greeting():
    print('Hello stdout world!!')

win = Frame()
win.pack()
# Label(win, text='hello container world').pack(side=TOP)
Button(win, text='Hello', command=greeting).pack(side=LEFT, anchor=N)
Label(win, text='hello container world').pack(side=TOP)
Button(win, text='Quit', command=win.quit).pack(side=RIGHT)

win.mainloop()