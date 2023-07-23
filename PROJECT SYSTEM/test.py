from tkinter import *
import tkinter as tk


def movebtn():
    global button_x
    button_x += 0.5
    buttonwid.place(relx=button_x, rely=0.5, anchor=CENTER)


window = Tk()
window.geometry("500x500")



button_x = 0.5
buttonwid = Button(window, text="LOL")
buttonwid.place(relx=button_x, rely=0.5, anchor=CENTER)

window.mainloop()