from tkinter import *
from time import strftime
import ttkbootstrap as ttk
root = Tk()


picker = ttk.DateEntry(root,bootstyle="danger")
picker.pack()


btn = Button(root, text="GET DATE",command=lambda:show())
btn.pack()

def show():
    sa = picker.entry.get()
    print(sa)


root.mainloop()