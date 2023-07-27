from tkinter import *
import customtkinter as MD


root = Tk()
root.geometry("100x200")


scroll = MD.CTkScrollableFrame(root)
scroll.pack()

signup = Frame(scroll, height=500, width=80,highlightbackground="Green", highlightcolor="Green", highlightthickness=2)
signup.pack()


a = Label(signup, text="USER SIGNUP")
a.place(x=0, y=0)







root.mainloop()