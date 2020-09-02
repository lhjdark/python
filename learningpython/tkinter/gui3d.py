import sys
from tkinter import *


class HelloClass:
    def __init__(self):
        self.msg = 'Hello __call__ world'

    def __call__(self):
        print(self.msg)
        sys.exit()


widget = Button(None, text="hello gui3d world", command=HelloClass())
widget.pack()
widget.mainloop()
