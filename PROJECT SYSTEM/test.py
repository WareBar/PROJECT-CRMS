from tkinter import *

#animation to move forward
def forward():
    global xcor
    if xcor != 400:
        
        xcor+=4
        button_forward.place(x=xcor, y=200)

        if xcor < 400:
            root.after(2, forward)
        else:
            print("STOP")
    else:
        print("STOP")

def backward():
    global ycor
    if ycor != 200:
        ycor -= 4
        button_backward.place(x=ycor, y=250)
        if ycor > 200:
            root.after(2, backward)
        else:
            print("STOP")
    else:
        print("STOP")





def both():
    forward()
    backward()





root = Tk()
root.geometry("600x400")


#RETRACTABLE FRAME
frameward=300



animatedframe = Frame(root,height=100, width=100, highlightbackground="Green", highlightcolor="Green", highlightthickness="4")
animatedframe.place(x=frameward, y=10)
indicator = 0

def framefward():
    global frameward
    if frameward != 500:
        frameward += 4
        animatedframe.place(x=frameward, y=10)
        if frameward < 500:
            root.after(10, framefward)
        else:
            print("STOP ME")


def frameBWARD():
    global frameward
    if frameward != 300:
        frameward -= 4
        animatedframe.place(x=frameward, y=10)
        if frameward > 300:
            root.after(10, frameBWARD)
        else:
            print("STOP ME")
"""
def retract():
    global indicator
    indicator+=1
    if (indicator % 2) == 0:
        framefward()
    else:
        frameBWARD()
"""












xcor = 300
ycor = 300

button_forward = Button(root, text="FORWARD")
button_forward.place(x=xcor, y=200)

button_backward = Button(root, text="BACKWARD")
button_backward.place(x=ycor, y=250)

controller = Button(root, text="COMMENCE")
controller.place(x=300, y=300)

controller.bind("<Enter>", framefward())
#controller.bind("<Leave>", frameBWARD())



root.mainloop()