from tkinter import *
import tkinter as tk
import customtkinter as MD


app = Tk()


crimes = ["Murder","Manslaughter","Assault","Robbery","Kidnapping","Rape","Domestic Violence","Burgarly","Theft","Larceny","Arson","Fraud","Identity theft","Hacking","Online Fraud"]

combobox_var = StringVar(value=crimes[0])
combobox = MD.CTkOptionMenu(app, values=crimes, variable=combobox_var,corner_radius=0, button_color="Black", dropdown_fg_color="White", dropdown_font=("Agency FB", 20, "bold"))
#combobox_var.set("option 2")
combobox.pack()

print(combobox_var.get())



app.mainloop()
