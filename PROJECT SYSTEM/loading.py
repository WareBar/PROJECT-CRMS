from tkinter import *
import tkinter as tk
from customtkinter import *
import customtkinter as MD
from PIL import ImageTk, Image
import time
from tkinter import ttk

#LOADINNG ANIMATION
origin = Tk()
origin.overrideredirect(1)
#size of window and coordinates
taas = 500
wide = 300
xcor = 430
ycor = 80

origin.geometry(f"{taas}x{wide}+{xcor}+{ycor}")
origin.update_idletasks()

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

dot1 = Image.open("photos/loaddots/4.png")
dot1 = dot1.resize((20,20), Image.LANCZOS)
dot1 = ImageTk.PhotoImage(dot1)

dot2 = Image.open("photos/loaddots/3.png")
dot2 = dot2.resize((20,20), Image.LANCZOS)
dot2 = ImageTk.PhotoImage(dot2)

dot3 = Image.open("photos/loaddots/2.png")
dot3 = dot3.resize((20,20), Image.LANCZOS)
dot3 = ImageTk.PhotoImage(dot3)

dot4 = Image.open("photos/loaddots/1.png")
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
while start < 5:
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
LogSign = Toplevel()
LogSign.geometry("700x550+100+20")
LogSign.overrideredirect(1)
LogSign.config(bg="#141414")





btn = Image.open("photos/logo.png")
btn = btn.resize((250, 250), Image.LANCZOS)
btn = ImageTk.PhotoImage(btn)
systemlogo = Label(LogSign, image=btn, bg="#141414")
systemlogo.place(x=225, y=80)

loginbtn = MD.CTkButton(LogSign, text="LOG IN", font=(("Plantagenet Cherokee",16,"bold")), bg_color="Grey",fg_color="Grey",hover_color="Black",corner_radius=0,command=lambda:slideleft())
loginbtn.place(x=285, y=340)



x_axis = 700
login = MD.CTkFrame(LogSign, height=400, width=350, bg_color="#141414", corner_radius=10)
login.place(x=x_axis, y=70)


a = Label(login, text="USER LOGIN", font=("Aharoni", 20), bg="White")
a.place(relx=0.250, rely=0.05)

b = Entry(login, width=37, bd=0, font=("Ariel", 10, "bold"))
b.place(relx=0.12, rely=0.3, relheight=0.08)

c = Entry(login, width=37, bd=0, show="*", font=("Ariel", 10, "bold"))
c.place(relx=0.12, rely=0.5, relheight=0.08)

"""
d = ttk.Checkbutton(login, text="Remember me")
d.place(x=32, y=240)
"""
e = MD.CTkButton(login, text="LOG IN", font=("Plantagenet Cherokee", 16), width=272, hover_color="Red", bg_color="White",corner_radius=0,command=lambda:interface())
e.place(relx=0.1, rely=0.7, relheight=0.08)

f = MD.CTkButton(login, text="Cancel", font=("Plantagenet Cherokee", 16), width=272, hover_color="Red", bg_color="White",corner_radius=0,command=lambda:slideright())
f.place(relx=0.1, rely=0.8, relheight=0.08)

g = MD.CTkButton(login, text="Forgot password?", font=("Ariel", 10), width=272, hover_color="Red", text_color="Black",fg_color="White",bg_color="White",corner_radius=0,command=lambda:interface())
g.place(relx=0.1, rely=0.9, relheight=0.08)

#g = Label(login, text="Don't have an account? Register", font=("Ariel", 10), bg="White")
#g.place(relx=0.2, rely=0.9)

linesimg = Image.open("photos/linya.PNG")
lineimg = linesimg.resize((270,2), Image.ANTIALIAS)
lineimg = ImageTk.PhotoImage(lineimg)


ID = Label(login, image=lineimg)
ID.place(relx=0.1, rely=0.375)

keycode = Label(login, image=lineimg)
keycode.place(relx=0.1, rely=0.575)



#CREATING THE ANIMATION FOR USER ID LABEL
def moveup():
    global ycor
    if ycor != 100:
        ycor -=1
        user.place(x=35, y=ycor)
        if ycor > 100:
            login.after(5, moveup)
        else:
                print("FLOWN")
    


def moveback():
    global ycor
    if ycor != 123:
        ycor += 1
        user.place(x=35, y=ycor)
        if ycor < 123:
            login.after(5, moveback)
        else:
            print("LANDED")

indicator = 0
def animation(event):
    global indicator
    indicator += 1
    if indicator % 2 == 0:
        if len(b.get()) > 0:
            1+1
        else:
            moveback()
    else:
        moveup()

#CREATING ANIMATION FOR PASSCODE LABEL


def go_up():
    global codecor
    if codecor != 180:
        codecor -= 1
        passcode.place(x=35, y=codecor)
        if codecor > 180:
            login.after(5, go_up)
        else:
            print("ON")

def go_down():
    global codecor
    if codecor != 203:
        codecor += 1
        passcode.place(x=35, y=codecor)
        if codecor < 203:
            login.after(5, go_down)
        else:
            print("OFF")

switch = 0
def anotheranimation(event):
    global switch
    switch += 1
    if switch % 2 == 0:
        if len(c.get()) > 0:
            1+1
        else:
            go_down()
    else:
        go_up()




#usecor = 100
ycor = 123
user = Label(login, text="USER ID", bg="White", font=("Corbel", 13,"bold"))
user.place(x=35, y=ycor)

#passcor = 180
codecor = 203
passcode = Label(login, text="PASSCODE",bg="White", font=("Corbel", 13,"bold"))
passcode.place(x=35, y=codecor)

b.bind("<Enter>", animation)
b.bind("<Leave>", animation)

c.bind("<Enter>", anotheranimation)
c.bind("<Leave>", anotheranimation)


#340
#700
#ANIMATE THE FRAME

def slideleft():
    global x_axis
    if x_axis != 340:
        x_axis -= 10
        login.place(x=x_axis, y=70)
        if x_axis > 340:
            LogSign.after(10, slideleft)

def slideright():
    global x_axis
    if x_axis != 700:
        x_axis += 10
        login.place(x=x_axis, y=70)
        if x_axis < 700:
            LogSign.after(10, slideright)







def interface():
    global maininterface
    maininterface = Toplevel()





origin.mainloop()