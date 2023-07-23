from tkinter import *
import tkinter as tk
from customtkinter import *
import customtkinter as MD
from PIL import ImageTk, Image
import ttkbootstrap as ttk
import time



origin = Tk()
origin.update_idletasks()
#size of window and coordinates
taas = 500
wide = 300
xcor = 430
ycor = 80

origin.geometry(f"{taas}x{wide}+{xcor}+{ycor}")
origin.config(bg="#141414")

btn = Image.open("photos/logo.png")
btn = btn.resize((150, 150), Image.LANCZOS)
btn = ImageTk.PhotoImage(btn)


systemlogo = Label(origin, image=btn, bg="#141414")
systemlogo.place(x=170, y=20)

title = Label(origin, text="C R M S", fg="#004FFF", bg="#141414", font=(20,20,))
title.place(x=193, y=160)


#line = Label(origin, text="_______", fg="#004FFF", bg="#141414", font=(20,20,))
#line.place(x=193, y=10, relheight=0.0)







for i in range(3):
    a = Label(origin, text="A").place(x=200, y=200)
    time.sleep(0.5)
    origin.update_idletasks()
    b = Label(origin, text="--").place(x=220, y=200)
    time.sleep(0.5)
    origin.update_idletasks()
    c = Label(origin, text="--").place(x=240, y=200)
    time.sleep(0.5)
    origin.update_idletasks()
    d = Label(origin, text="--").place(x=260, y=200)
    time.sleep(0.5)
    origin.update_idletasks()




    a = Label(origin, text="--").place(x=200, y=200)
    time.sleep(0.5)
    origin.update_idletasks()
    b = Label(origin, text="A").place(x=220, y=200)
    time.sleep(0.5)
    origin.update_idletasks()
    c = Label(origin, text="--").place(x=240, y=200)
    time.sleep(0.5)
    origin.update_idletasks()
    d = Label(origin, text="--").place(x=260, y=200)
    time.sleep(0.5)
    origin.update_idletasks()




    a = Label(origin, text="--").place(x=200, y=200)
    time.sleep(0.5)
    origin.update_idletasks()
    b = Label(origin, text="--").place(x=220, y=200)
    time.sleep(0.5)
    origin.update_idletasks()
    c = Label(origin, text="A").place(x=240, y=200)
    time.sleep(0.5)
    origin.update_idletasks()
    d = Label(origin, text="--").place(x=260, y=200)
    origin.update_idletasks()


















"""
loading = Frame(origin, height=20, width=110, highlightbackground="Green", highlightcolor="Green", highlightthickness=1)
loading.place(x=193, y=195)





for i in range(5):
    a = Label(loading, text="0").place(x=0, y=0)
    b = Label(loading, text="--").place(x=20, y=0)
    c = Label(loading, text="--").place(x=40, y=0)
    d = Label(loading, text="--").place(x=60, y=0)
    time.sleep(0.5)
    origin.update_idletasks()
    loading.update_idletasks()

    a = Label(loading, text="--").place(x=0, y=0)
    b = Label(loading, text="0").place(x=20, y=0)
    c = Label(loading, text="--").place(x=40, y=0)
    d = Label(loading, text="--").place(x=60, y=0)
    time.sleep(0.5)
    origin.update_idletasks()
    loading.update_idletasks()

    a = Label(loading, text="--").place(x=0, y=0)
    b = Label(loading, text="--").place(x=20, y=0)
    c = Label(loading, text="0").place(x=40, y=0)
    d = Label(loading, text="--").place(x=60, y=0)
    time.sleep(0.5)
    origin.update_idletasks()
    loading.update_idletasks()

    a = Label(loading, text="--").place(x=0, y=0)
    b = Label(loading, text="--").place(x=20, y=0)
    c = Label(loading, text="--").place(x=40, y=0)
    d = Label(loading, text="00").place(x=60, y=0)
    time.sleep(0.5)
    origin.update_idletasks()
    loading.update_idletasks()
"""









origin.update_idletasks()
startnotice = Label(origin, text="Starting...", bg="#141414", fg="White", font=((23)))
startnotice.place(x=0, y=275)
origin.update_idletasks()

origin.mainloop()