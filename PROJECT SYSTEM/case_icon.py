from tkinter import *
import tkinter as tk
from customtkinter import *
import customtkinter as MD
from PIL import ImageTk, Image
import time
from tkinter import ttk
from tkvideo import tkvideo
from openpyxl import load_workbook
from openpyxl import *
from tkinter import messagebox
from functools import partial



root = Tk()
root.geometry("400x400")


frame = Frame(root, width=130, height=130,bg="#545454")
frame.place(relx=0.2, rely=0.2)

own_logo = Image.open("photos/case_logo.png")
own_logo = own_logo.resize((130,130), Image.ANTIALIAS)
own_logo = ImageTk.PhotoImage(own_logo)


s = MD.CTkButton(frame, text=None,image=own_logo, width=50, height=50,fg_color="#545454", hover_color="Red")
s.pack()

a = MD.CTkLabel(l, text="CRIME CASE #1")
a.pack(side=BOTTOM)


root.mainloop()