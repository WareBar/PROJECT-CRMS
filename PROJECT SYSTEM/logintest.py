import customtkinter as MD


root = MD.CTk()
root.geometry("400x200")



xcor = 400
myframe = MD.CTkFrame(root, height=100, width=100, fg_color="Grey", corner_radius=0)
myframe.place(x=xcor, y=20)
indicator = 0

#MAIN FUNCTIONS
def slideFrame():
    global indicator
    indicator += 1
    if (indicator % 2) == 0:
        left()
    else:
        right()
    

def left():
    global xcor
    if xcor != 300:
        xcor -= 4
        myframe.place(x=xcor, y=20)
        if xcor > 300:
            root.after(10,left)
        else:
            print("STOP")

def right():
    global xcor
    if xcor != 400:
        xcor += 4
        myframe.place(x=xcor, y=20)
        if xcor < 400:
            root.after(10,right)
        else:
            print("STOP")

login = MD.CTkButton(root, text="LOG IN", command=lambda:slideFrame())
login.place(x=20, y=20)


root.mainloop()