from menu_frm import makemenu
from tkinter import *

root = Tk()
for i in range(3):
    frm = Frame()
    mnu = makemenu(frm)
    frm.pack(expand=YES, fill=BOTH)
    Label(frm, bg='YELLOW', height=5, width=25).pack(expand=YES, fill=BOTH)
Button(root, text='Bye', command=root.quit).pack()
root.mainloop()