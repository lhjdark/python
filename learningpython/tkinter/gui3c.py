''' Bound 方法回调处理器'''

import sys
from tkinter import *

class HelloClass:
    def __init__(self):
        widget = Button(None, text='Hello Bound world', command=self.quit)
        widget.pack()

    def quit(self):
        print('Hello class mothed world')
        sys.exit()


HelloClass()
mainloop()