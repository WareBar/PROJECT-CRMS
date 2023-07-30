import tkinter as tk
from functools import partial
from tkinter import messagebox



def button_click(number):
    messagebox.showerror("SELECTED",f"CRIME CASE #{number}")



root = tk.Tk()

buttons = []  # List to store the buttons

for i in range(5):
    button = tk.Button(root, text="Button " + str(i), command=partial(button_click, i))
    button.pack()
    buttons.append(button)  # Add the button to the list









root.mainloop()
