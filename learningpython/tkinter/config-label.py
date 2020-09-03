from tkinter import *

root = Tk()
labelFont = ('times', 20, 'bold')
widget = Label(root, text='Hello config world')
widget.config(bg='red', fg='yellow')
widget.config(font=labelFont)
widget.config(height=10, width=40)
widget.config(bd=5, relief=GROOVE, cursor='watch')
widget.config(padx=5, pady=6)
widget.pack(expand=YES, fill=BOTH)
root.mainloop()