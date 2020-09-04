from tkinter import *
from entry2 import makeform, fetch, fields


def show(entries, popup):
    fetch(entries)
    popup.destroy()

def ask():
    popup = Toplevel()
    ents = makeform(popup, fields)
    Button(popup, text='OK', command=(lambda : show(ents, popup))).pack()
    popup.grab_set()
    popup.focus_set()
    popup.wait_window()

root = Tk()
Label(root, text='电信宽带1').pack(side=TOP)
Button(root, text='新合同录入1', command=ask).pack(side=TOP)
# Label(root, text='电信宽带2').pack(side=LEFT)
# Button(root, text='新合同录入1', command=ask).pack(side=LEFT)
root.mainloop()

