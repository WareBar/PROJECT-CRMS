from tkinter import *
from tkcalendar import *

root = Tk()
root.geometry("300x300")

taas = 0
xcor = 0
FRAME = Frame(root, height=taas,width=270,highlightbackground="Green", highlightcolor="Green", highlightthickness=5)
FRAME.place(x=xcor, y=0)









def show(event):
    taas = 200
    FRAME = Frame(root, height=taas,width=270,highlightbackground="Green", highlightcolor="Green", highlightthickness=5)
    FRAME.place(x=xcor, y=0)

    date = Calendar(FRAME, setmode="day", date_pattern="d/m/yy")
    date.place(x=0, y=0)
    








btn = Button(root, text="SHOW")
btn.pack(side="bottom")

btn.bind("<Enter>", show)




root.mainloop()