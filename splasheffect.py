from tkinter import *
import tkinter as tk
import time



root = Tk()
root.geometry("200x200")


for i in range(5):
    a = Label(root, text="A").place(x=0, y=0)
    time.sleep(0.5)
    root.update_idletasks()
    b = Label(root, text="B").place(x=20, y=20)
    time.sleep(0.5)
    root.update_idletasks()
    c = Label(root, text="C").place(x=40, y=40)
    time.sleep(0.5)
    root.update_idletasks()
    d = Label(root, text="D").place(x=60, y=60)
    time.sleep(0.5)
    root.update_idletasks()







root.mainloop()