import sys
from tkinter import *

def handler(p1, p2):
    print(p1, p2)


widget = Button(None, text='Hello lambdas world', command=(lambda: handler('hello', 'wazzzzzz'))  )
widget.pack()
widget.mainloop()