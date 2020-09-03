import sys
from tkinter import Toplevel, Button, Label

win1 = Toplevel()
win2 = Toplevel()
Button(win1, text='aaaa', command=sys.exit).pack()
Button(win2, text='bbbb', command=sys.exit).pack()
Label(text='Popups').pack()
win1.mainloop()