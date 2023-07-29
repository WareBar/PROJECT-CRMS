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





CRMS = Tk()
CRMS.geometry("1200x700")
CRMS.config(bg="#000000")



CRMS_LOGO = Image.open("photos/LINES.png")
CRMS_LOGO = CRMS_LOGO.resize((50,50), Image.ADAPTIVE)
CRMS_LOGO = ImageTk.PhotoImage(CRMS_LOGO)



system_upframe = Frame(CRMS, width=1200, height=50, bg="#545454")
system_upframe.place(x=0, y=0)

system_logo_label = Label(CRMS, image=CRMS_LOGO, bg="#545454")
system_logo_label.place(x=10, y=0)



system_uplabel = Label(system_upframe, text="CRIME RECORD MANAGEMENT SYSTEM", bg="#545454", fg="#D9D9D9",font=("Agency FB", 20, "bold"))
system_uplabel.place(x=60, y=4)



SEARCH_FRAME = MD.CTkFrame(CRMS, width=725, height=40, bg_color="#000000",corner_radius=8)
SEARCH_FRAME.place(x=30, y=100)

search_box = MD.CTkEntry(SEARCH_FRAME,fg_color="#141414", text_color="White", font=("Agency FB", 20, "bold"))
search_box.place(x=550,y=4,relwidth=0.2,relheight=0.82)

#IMPORTING THE IMAGE

search_icon = MD.CTkImage(light_image = Image.open("photos/search_icon.png"), size=(15,15))

search_button = MD.CTkButton(SEARCH_FRAME,image=search_icon, text=None, width=5,height=10,fg_color="#141414", bg_color="#141414",hover_color="Black")
search_button.place(x=648, y=8,relwidth=0.06)

CASE_FRAME = MD.CTkScrollableFrame(CRMS, width=700, height=500, bg_color="#000000",corner_radius=8)
CASE_FRAME.place(x=30, y=150)

GRAPH_FRAME = MD.CTkFrame(CRMS, width=380, height=515, bg_color="#000000",corner_radius=8)
GRAPH_FRAME.place(x=800, y=150)



CASE_CANVAS = Canvas(CASE_FRAME, width="680", height=1200)
CASE_CANVAS.grid_propagate(False)
CASE_CANVAS.grid(row=0, column=0)


#ls = Label(CASE_CANVAS, text="CASE FILES")
#ls.pack()



for i in range(int(8/2)):
    for j in range(4):
        l = Button(CASE_CANVAS, text="CASE NUMBER#1", command=lambda:show_case())
        #l.pack()
        l.grid(row=i, column=j, padx=20, pady=20)



def show_case():
    messagebox.showinfo("CASE FILES",f"SUSPECT: VARRY\nVICTIM: MADONA")








CRMS.mainloop()