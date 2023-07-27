from tkinter import *
import customtkinter as MD
from tkinter import ttk
from PIL import Image, ImageTk

signup = Tk()
signup.geometry("665x400")
signup.config(bg="#D9D9D9")
#root.overrideredirect(1)

FRAME = MD.CTkScrollableFrame(signup, width=605, height=350, bg_color="Red", fg_color="#D9D9D9",corner_radius=20)
FRAME.place(x=4, y=4)

CANVAS = Canvas(FRAME, width=620, height=600, highlightbackground="#D9D9D9", background="#D9D9D9")
CANVAS.pack(fill=BOTH)











signtitle = Label(CANVAS, text="USER SIGNUP", font=("Cambria", 20), bg="#D9D9D9")
signtitle.place(relx=0.370, rely=0.1)

entry_height = 0.06






name = Entry(CANVAS, width=37, bd=0, font=("Ariel", 10, "bold"), bg="#D9D9D9")
name.place(x=26, y=160, relheight=entry_height)

Identification = Entry(CANVAS, width=37, bd=0, font=("Ariel", 10, "bold"), bg="#D9D9D9")
Identification.place(x=350, y=160, relheight=entry_height)

email = Entry(CANVAS, width=37, bd=0, font=("Ariel", 10, "bold"), bg="#D9D9D9")
email.place(x=26, y=240, relheight=entry_height)

password = Entry(CANVAS, width=37, bd=0, font=("Ariel", 10, "bold"), bg="#D9D9D9")
password.place(x=350, y=240, relheight=entry_height)

confirmpassword = Entry(CANVAS, width=37, bd=0, font=("Ariel", 10, "bold"), bg="#D9D9D9")
confirmpassword.place(x=350, y=320, relheight=entry_height)

phonenumber = Entry(CANVAS, width=37, bd=0, font=("Ariel", 10, "bold"), bg="#D9D9D9")
phonenumber.place(x=26, y=320, relheight=entry_height)

dateofbirth = Entry(CANVAS, width=37, bd=0, font=("Ariel", 10, "bold"), bg="#D9D9D9")
dateofbirth.place(x=26, y=400, relheight=entry_height)

zipcode = Entry(CANVAS, width=37, bd=0, font=("Ariel", 10, "bold"), bg="#D9D9D9")
zipcode.place(x=350, y=400, relheight=entry_height)

linesimg = Image.open("photos/linya.PNG")
lineimg = linesimg.resize((255,2), Image.LANCZOS)
lineimg = ImageTk.PhotoImage(lineimg)


#LABEL TO ANIMATE
#VARIABLES FOR Y COORDINATE OF EACH LABEL
firstrow = 160
secondrow = 240
thirdrow = 320
fourthrow = 400




fullname = Label(CANVAS, text="FULL NAME",font=("Corbel", 13,"bold"), bg="#D9D9D9")
fullname.place(x=26, y=firstrow)
line = Label(CANVAS, image=lineimg)
line.place(x=25, y=190)

ID = Label(CANVAS, text="USER ID",font=("Corbel", 13,"bold"), bg="#D9D9D9")
ID.place(x=350,y=firstrow)
line = Label(CANVAS, image=lineimg)
line.place(x=349, y=190)


mail = Label(CANVAS, text="EMAIL",font=("Corbel", 13,"bold"), bg="#D9D9D9")
mail.place(x=26,y=secondrow)
line = Label(CANVAS, image=lineimg)
line.place(x=25, y=270)

word = Label(CANVAS, text="PASSWORD",font=("Corbel", 13,"bold"), bg="#D9D9D9")
word.place(x=350,y=secondrow)
line = Label(CANVAS, image=lineimg)
line.place(x=349, y=270)

conword = Label(CANVAS, text="CONFIRM PASSWORD",font=("Corbel", 13,"bold"), bg="#D9D9D9")
conword.place(x=350,y=thirdrow)
line = Label(CANVAS, image=lineimg)
line.place(x=349, y=350)

phonenum = Label(CANVAS, text="PHONE NUMBER",font=("Corbel", 13,"bold"), bg="#D9D9D9")
phonenum.place(x=26,y=thirdrow)
line = Label(CANVAS, image=lineimg)
line.place(x=25, y=350)

bday = Label(CANVAS, text="DATE OF BIRTH",font=("Corbel", 13,"bold"), bg="#D9D9D9")
bday.place(x=26,y=fourthrow)
line = Label(CANVAS, image=lineimg)
line.place(x=25, y=430)

Zcode = Label(CANVAS, text="ZipCode",font=("Corbel", 13,"bold"), bg="#D9D9D9")
Zcode.place(x=350,y=fourthrow)
line = Label(CANVAS, image=lineimg)
line.place(x=349, y=430)

#####################################-------------ANIMATING THE LABEL WIDGETS-------------------###########################

#-------------------------------------------------NAME LABEL ANIMATION BELOW-------------------------------------------------
#NAME LABEL
#for label NAME to go up
def nameup():
    global firstrow
    if firstrow != 142:
        firstrow-=1
        fullname.place(x=26, y=firstrow)
        if firstrow > 142:
            signup.after(10, nameup)

#for label NAME to go down

def namedown():
    global firstrow
    if firstrow != 160:
        firstrow +=1
        fullname.place(x=26, y=firstrow)
        if firstrow < 160:
            signup.after(10, namedown)

#ANIMATION FUNCTION OF NAME LABEL
name_indicator = 0
def name_animation(event):
    global name_indicator
    name_indicator += 1
    if (name_indicator % 2)==0:
        if len(name.get())>0:
            1+1
        else:
            namedown()
    else:
        nameup()
        
name.bind("<Enter>", name_animation)
name.bind("<Leave>", name_animation)
#-----------------------------------------------NAME LABEL ANIMATION ABOVE-------------------------------------------------




#-----------------------------------------------USER LABEL ANIMATION BELOW-------------------------------------------------

#USER ID
#for label USER ID to go up

def user_up():
    global firstrow
    if firstrow != 142:
        firstrow -= 1
        ID.place(x=350,y=firstrow)
        if firstrow > 142:
            signup.after(10,user_up)
        else:
            print("DAP")


def user_down():
    global firstrow
    if firstrow != 160:
        firstrow += 1
        ID.place(x=350,y=firstrow)
        if firstrow < 160:
            signup.after(10,user_down)
        else:
            print("DOP")

user_indicator = 0
def user_animation(event):
    global user_indicator
    user_indicator+=1
    if (user_indicator % 2)==0:
        if len(Identification.get())>0:
            1+1
        else:
            user_down()
    else:
        user_up()




Identification.bind("<Enter>", user_animation)
Identification.bind("<Leave>", user_animation)
#-----------------------------------------------USER LABEL ANIMATION ABOVE-------------------------------------------------

#-----------------------------------------------EMAIL LABEL ANIMATION BELOW-------------------------------------------------

#to go up
def mail_up():
    global secondrow
    if secondrow != 222:
        secondrow -= 1
        mail.place(x=26,y=secondrow)
        if secondrow > 222:
            signup.after(10, mail_up)
#TO GO DOWN
def mail_down():
    global secondrow
    if secondrow != 240:
        secondrow += 1
        mail.place(x=26,y=secondrow)
        if secondrow < 240:
            signup.after(10, mail_down)


mail_indicator = 0

def mail_animation(event):
    global mail_indicator
    mail_indicator += 1
    if (mail_indicator % 2) == 0:
        if len(email.get())>0:
            #DO NOTHING
            1+1
        else:
            mail_down()
    else:
        mail_up()


email.bind("<Enter>", mail_animation)
email.bind("<Leave>", mail_animation)



#-----------------------------------------------EMAIL LABEL ANIMATION ABOVE-------------------------------------------------

#-----------------------------------------------PASSWORD LABEL ANIMATION BELOW-------------------------------------------------
#TO GO UP
def pass_up():
    global secondrow
    if secondrow != 222:
        secondrow -= 1
        word.place(x=350,y=secondrow)
        if secondrow > 222:
            signup.after(10, pass_up)

#TO GO DOWN
def pass_down():
    global secondrow
    if secondrow != 240:
        secondrow += 1
        word.place(x=350,y=secondrow)
        if secondrow < 240:
            signup.after(10, pass_down)

password_indicator = 0
def password_animation(event):
    global password_indicator
    password_indicator += 1
    if (password_indicator % 2)==0:
        if len(password.get())>0:
            #do nothing
            1+1
        else:
            pass_down()
    else:
        pass_up()

password.bind("<Enter>", password_animation)
password.bind("<Leave>", password_animation)

#-----------------------------------------------PASSWORD LABEL ANIMATION ABOVE-------------------------------------------------

#---------------------------------------------PHONE NUMBER LABEL ANIMATION BELOW-------------------------------------------------
#TO GO UP
def phone_up():
    global thirdrow
    if thirdrow != 302:
        thirdrow -= 1
        phonenum.place(x=26,y=thirdrow)
        if thirdrow > 302:
            signup.after(10, phone_up)
    
#TO GO DOWN
def phone_down():
    global thirdrow
    if thirdrow != 320:
        thirdrow += 1
        phonenum.place(x=26,y=thirdrow)
        if thirdrow < 320:
            signup.after(10, phone_down)

phone_label_indicator = 0
def phone_label_animation(event):
    global phone_label_indicator
    phone_label_indicator+=1
    if (phone_label_indicator % 2) == 0:
        phone_down()
    else:
        phone_up()

phonenumber.bind("<Enter>", phone_label_animation)
phonenumber.bind("<Leave>", phone_label_animation)

        
#---------------------------------------------PHONE NUMBER LABEL ANIMATION ABOVE-------------------------------------------------

#----------------------------------------CONFIRM PASSWORD NUMBER LABEL ANIMATION BELOW-------------------------------------------------
#TO GO UP
def confirm_up():
    global thirdrow
    if thirdrow != 302:
        thirdrow -= 1
        conword.place(x=350,y=thirdrow)
        if thirdrow > 302:
            signup.after(10, confirm_up)

#TO GO DOWN
def confirm_down():
    global thirdrow
    if thirdrow != 320:
        thirdrow += 1
        conword.place(x=350,y=thirdrow)
        if thirdrow < 320:
            signup.after(10, confirm_down)


confirm_indicator = 0
def confirm_pass_animation(event):
    global confirm_indicator
    confirm_indicator += 1
    if (confirm_indicator % 2)==0:
        if len(confirmpassword.get())>0:
            #do nothing
            1+1
        else:
            confirm_down()
    else:
        confirm_up()

confirmpassword.bind("<Enter>", confirm_pass_animation)
confirmpassword.bind("<Leave>", confirm_pass_animation)


#----------------------------------------CONFIRM PASSWORD NUMBER LABEL ANIMATION ABOVE-------------------------------------------------

#----------------------------------------BIRTHDAY LABEL ANIMATION BELOW-------------------------------------------------
#TO GO UP
def date_up():
    global fourthrow
    if fourthrow != 382:
        fourthrow -= 1
        bday.place(x=26,y=fourthrow)
        if fourthrow > 382:
            signup.after(10, date_up)

#TO GO DOWN
def date_down():
    global fourthrow
    if fourthrow != 400:
        fourthrow += 1
        bday.place(x=26,y=fourthrow)
        if fourthrow < 400:
            signup.after(10, date_down)

date_indicator = 0
def date_animation(event):
    global date_indicator
    date_indicator+=1
    if (date_indicator%2)==0:
        if len(dateofbirth.get())>0:
            #do nothing
            1+1
        else:
            date_down()
    else:
        date_up()

dateofbirth.bind("<Enter>", date_animation)
dateofbirth.bind("<Leave>", date_animation)



#----------------------------------------BIRTHDAY LABEL LABEL ANIMATION ABOVE-------------------------------------------------

#----------------------------------------ZIPCODE LABEL LABEL ANIMATION BELOW-------------------------------------------------

def code_up():
    global fourthrow
    if fourthrow != 382:
        fourthrow -= 1
        Zcode.place(x=350,y=fourthrow)
        if fourthrow > 382:
            signup.after(10, code_up)

def code_down():
    global fourthrow
    if fourthrow != 400:
        fourthrow += 1
        Zcode.place(x=350,y=fourthrow)
        if fourthrow < 400:
            signup.after(10, code_down)

Zindicator = 0
def Zcode_animation(event):
    global Zindicator
    Zindicator += 1
    if (Zindicator % 2)==0:
        if len(zipcode.get())>0:
            #do nothing
            1+1
        else:
            code_down()
    else:
        code_up()

zipcode.bind("<Enter>", Zcode_animation)
zipcode.bind("<Leave>", Zcode_animation)



#----------------------------------------ZIPCODE LABEL LABEL ANIMATION ABOVE-------------------------------------------------





#BUTTONS
register = MD.CTkButton(CANVAS, text="REGISTER", font=("Agency FB", 30, "bold"),text_color="Black",fg_color="#61777B",corner_radius=0)
register.place(x=26, y=450, relwidth=0.41,relheight=entry_height)

cancelregister = MD.CTkButton(CANVAS, text="CANCEL", font=("Agency FB", 30, "bold"),text_color="Black",fg_color="#61777B",corner_radius=0)
cancelregister.place(x=350, y=450, relwidth=0.41,relheight=entry_height)
















signup.mainloop()