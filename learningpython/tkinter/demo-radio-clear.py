from tkinter import *
root = Tk()
def radio1():
    #global tmp
    tmp = IntVar(0)
    for i in range(0, 10):
        rad = Radiobutton(root, text=str(i), value=i, variable=tmp)
        rad.pack(side=LEFT)
    tmp.set(5)

radio1()
root.mainloop()