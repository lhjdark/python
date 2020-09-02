from tkinter import *
root = Tk()
Button(root, text='press-L', command=root.quit).pack(side=LEFT, expand=YES)
Button(root, text='press-R', command=root.quit).pack(side=RIGHT, expand=YES)

root.mainloop()