from tkinter import *
from PIL import ImageTk, Image
from customtkinter import *
import customtkinter as MD



root = Tk()
root.title("test")
root.geometry("380x515")



TITLE = Label(root, text="PROFILE",font=("Agency FB", 30, "bold"),bg="#A6A6A6")
TITLE.place(x=130, y=60)

show_name = Label(root, text="NAME:",font=("Agency FB", 20, "bold"),bg="#A6A6A6")
show_id = Label(root, text="USER ID:",font=("Agency FB", 20, "bold"),bg="#A6A6A6")
show_email = Label(root, text="EMAIL:",font=("Agency FB", 20, "bold"),bg="#A6A6A6")
show_phone_number = Label(root, text="PHONE NUMBER:",font=("Agency FB", 20, "bold"),bg="#A6A6A6")


show_name.place(x=20, y=140)

show_id.place(x=20,y=190)

show_email.place(x=20, y=240)

show_phone_number.place(x=20, y=290)


data = Label(root, text="DATA:",font=("Agency FB", 20, "bold"),bg="#A6A6A6")
data.place(x=170, y=140)





root.mainloop()