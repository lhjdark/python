import sys
from tkinter import *

def handler(p1, p2):
    print(p1, p2)

def makegui():
    X = 42
    Button(text='nnnnnn', command=(lambda X=X: handler(X, 'spam')))


widget = Button(None, text='Hello lambdas world', command=makegui)
widget.pack()
widget.mainloop()