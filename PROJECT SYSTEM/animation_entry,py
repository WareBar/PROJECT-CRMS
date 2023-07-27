from tkinter import *

root = Tk()
root.geometry("350x500")
root.config(bg="White")


def moveforward():
    global yaxis
    if yaxis != 200:
        yaxis -= 5
        label.place(x=100, y=yaxis)
        if yaxis > 200:
            root.after(10, moveforward)



def movebackward():
    global yaxis
    if yaxis != 300:
        yaxis += 5
        label.place(x=100, y=yaxis)
        if yaxis < 300:
            root.after(10, movebackward)



indicator = 0
def animation(event):
    global indicator
    indicator += 1
    if (indicator % 2):
        moveforward()
        print("SWTICH ON")
    else:
        movebackward()
        print("SWITCH OFF")
    print(indicator)
        





put = Entry(root, fg="Black")
put.place(x=100,y=100)

yaxis = 300
label = Label(root, text="ANIMATION")
label.place(x=100, y=yaxis)


put.bind("<Enter>", animation)
put.bind("<Leave>", animation)




root.mainloop()