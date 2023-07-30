from tkinter import *
import tkinter as tk
import customtkinter as MD
from PIL import Image, ImageTk


CASE_FILES = Tk()
CASE_FILES.geometry("400x500")
CASE_FILES.config(bg="#545454")


case_number = MD.CTkLabel(CASE_FILES, text="CRIME CASE #1", font=("Agency FB", 38, "bold"), bg_color="#545454", fg_color="#D9D9D9", corner_radius=7)
case_number.place(x=10, y=10)


suspect_name = MD.CTkLabel(CASE_FILES, text="SUSPECT:", font=("Agency FB", 30, "bold"), bg_color="#545454", fg_color="#545454", corner_radius=7)
suspect_name.place(x=10, y=60)

name_here = MD.CTkLabel(CASE_FILES, text="name here", font=("Agency FB", 30, "bold"), bg_color="#545454", fg_color="#545454", corner_radius=7)
name_here.place(x=110,y=60)

victims_name = MD.CTkLabel(CASE_FILES, text="VICTIM:", font=("Agency FB", 30, "bold"), bg_color="#545454", fg_color="#545454", corner_radius=7)
victims_name.place(x=10, y=100)

v_name_here = MD.CTkLabel(CASE_FILES, text="name here", font=("Agency FB", 30, "bold"), bg_color="#545454", fg_color="#545454", corner_radius=7)
v_name_here.place(x=110, y=100)

lines = Image.open("photos/linya.PNG")
lines = lines.resize((350,1), Image.LANCZOS)
lines = ImageTk.PhotoImage(lines)



lines = Label(CASE_FILES, image=lines)
lines.place(x=20, y=150)

crime_type = MD.CTkLabel(CASE_FILES, text="TYPE OF CRIMES:", font=("Agency FB", 30, "bold"), bg_color="#545454", fg_color="#545454", corner_radius=7)
crime_type.place(x=10, y=160)


yaxis = 160

for i in range(3):
    crimes = MD.CTkLabel(CASE_FILES, text="MURDER:", font=("Agency FB", 20, "bold"), bg_color="#545454", fg_color="#545454", corner_radius=7)
    crimes.place(x=210, y=yaxis)
    yaxis += 30





lines = Image.open("photos/linya.PNG")
lines = lines.resize((350,1), Image.LANCZOS)
lines = ImageTk.PhotoImage(lines)

lines = Label(CASE_FILES, image=lines)
lines.place(x=20, y=260)


occurence_location = MD.CTkLabel(CASE_FILES, text="LOCATION OF OCCURENCE:", font=("Agency FB", 20, "bold"), bg_color="#545454", fg_color="#545454", corner_radius=7)
occurence_location.place(x=10, y=290)

location_here = MD.CTkLabel(CASE_FILES, text="Lucena City, Quezon", font=("Agency FB", 20, "bold"), bg_color="#545454", fg_color="#545454", corner_radius=7)
location_here.place(x=190, y=290)

occurence_date = MD.CTkLabel(CASE_FILES, text="DATE OF OCCURENCE:", font=("Agency FB", 20, "bold"), bg_color="#545454", fg_color="#545454", corner_radius=7)
occurence_date.place(x=10, y=320)


data_here = MD.CTkLabel(CASE_FILES, text="July 4th", font=("Agency FB", 20, "bold"), bg_color="#545454", fg_color="#545454", corner_radius=7)
data_here.place(x=190, y=320)

narrative_report = MD.CTkLabel(CASE_FILES, text="NARRATIVE REPORT:", font=("Agency FB", 20, "bold"), bg_color="#545454", fg_color="#545454", corner_radius=7)
narrative_report.place(x=10, y=350)

box = MD.CTkTextbox(CASE_FILES, width=360, height=70,state=DISABLED)
box.place(x=15, y=380)


message = "JULY 4TH WHEN BARACK OBAM WAS KILLED BY SOME ASSASSIN NAMED BARRY A HACKER THAT WAS ANGERED BECAUSE OF OBAMA IRRATIONAL DECISION IN THE NATION SONA"

box.configure(state=NORMAL)
box.insert(1.0, message)
box.configure(state=DISABLED)



edit_button = MD.CTkButton(CASE_FILES, text="EDIT", font=("Agency FB", 30, "bold"), text_color="Black",bg_color="#545454", fg_color="#D9D9D9", corner_radius=5)
edit_button.place(x=15, y=455)

delete_button = MD.CTkButton(CASE_FILES, text="DELETE", font=("Agency FB", 30, "bold"), text_color="Black",bg_color="#545454", fg_color="#D9D9D9", corner_radius=5)
delete_button.place(x=235, y=455)


CASE_FILES.mainloop()