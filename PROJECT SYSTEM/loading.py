from tkinter import *
import tkinter as tk
from customtkinter import *
import customtkinter as MD
from PIL import ImageTk, Image
import time


#LOADINNG ANIMATION
origin = Tk()
#origin.overrideredirect(1)
#size of window and coordinates
taas = 500
wide = 300
xcor = 430
ycor = 80

origin.geometry(f"{taas}x{wide}+{xcor}+{ycor}")
origin.update_idletasks()

origin.config(bg="#141414")

btn = Image.open("PROJECT SYSTEM/photos/logo.png")
btn = btn.resize((150, 150), Image.LANCZOS)
btn = ImageTk.PhotoImage(btn)


systemlogo = Label(origin, image=btn, bg="#141414")
systemlogo.place(x=170, y=20)

title = Label(origin, text="C R M S", fg="#004FFF", bg="#141414", font=(20,20,))
title.place(x=193, y=160)


#line = Label(origin, text="_______", fg="#004FFF", bg="#141414", font=(20,20,))
#line.place(x=193, y=10, relheight=0.0)

dot1 = Image.open("PROJECT SYSTEM/photos/loaddots/4.png")
dot1 = dot1.resize((20,20), Image.LANCZOS)
dot1 = ImageTk.PhotoImage(dot1)

dot2 = Image.open("PROJECT SYSTEM/photos/loaddots/3.png")
dot2 = dot2.resize((20,20), Image.LANCZOS)
dot2 = ImageTk.PhotoImage(dot2)

dot3 = Image.open("PROJECT SYSTEM/photos/loaddots/2.png")
dot3 = dot3.resize((20,20), Image.LANCZOS)
dot3 = ImageTk.PhotoImage(dot3)

dot4 = Image.open("PROJECT SYSTEM/photos/loaddots/1.png")
dot4 = dot4.resize((20,20), Image.LANCZOS)
dot4 = ImageTk.PhotoImage(dot4)


dotmate1 = Label(origin, image=dot1, bg="#141414")
dotmate1.place(x=192, y=200)

dotmate2 = Label(origin, image=dot2, bg="#141414")
dotmate2.place(x=222, y=200)

dotmate3 = Label(origin, image=dot3, bg="#141414")
dotmate3.place(x=252, y=200)

dotmate4 = Label(origin, image=dot4, bg="#141414")
dotmate4.place(x=282, y=200)


origin.update_idletasks()
startnotice = Label(origin, text="Starting...", bg="#141414", fg="White", font=((23)))
startnotice.place(x=0, y=275)
time.sleep(0.5)


start = 0
for i in range(1,5):
    dotmate1.config(image=dot4)
    dotmate2.config(image=dot1)
    dotmate3.config(image=dot2)
    dotmate4.config(image=dot3)
    time.sleep(0.5)
    origin.update_idletasks()

    dotmate1.config(image=dot3)
    dotmate2.config(image=dot4)
    dotmate3.config(image=dot1)
    dotmate4.config(image=dot2)
    time.sleep(0.5)
    origin.update_idletasks()

    dotmate1.config(image=dot2)
    dotmate2.config(image=dot3)
    dotmate3.config(image=dot4)
    dotmate4.config(image=dot1)
    time.sleep(0.5)
    origin.update_idletasks()

    dotmate1.config(image=dot1)
    dotmate2.config(image=dot2)
    dotmate3.config(image=dot3)
    dotmate4.config(image=dot4)
    time.sleep(0.5)
    origin.update_idletasks()

    start += 1




origin.withdraw()
logsign = Toplevel()
logsign.geometry("1200x650+400+50")
logsign.config(bg="#141414")





btn = Image.open("PROJECT SYSTEM/photos/logo.png")
btn = btn.resize((450, 450), Image.LANCZOS)
btn = ImageTk.PhotoImage(btn)
systemlogo = Label(logsign, image=btn, bg="#141414")
systemlogo.place(x=350, y=100)










origin.mainloop()