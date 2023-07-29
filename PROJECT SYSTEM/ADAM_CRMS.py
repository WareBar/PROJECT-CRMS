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


#LOADINNG ANIMATION
origin = Tk()
origin.overrideredirect(1)
#size of window and coordinates
taas = 500
wide = 300
xcor = 750
ycor = 250

origin.geometry(f"{taas}x{wide}+{xcor}+{ycor}")
origin.update_idletasks()

origin.config(bg="#141414")

#-----------------------------------------------------------------FRONT END-------------------------------------------------

btn = Image.open("photos/logo.png")
btn = btn.resize((150, 150), Image.LANCZOS)
btn = ImageTk.PhotoImage(btn)


systemlogo = Label(origin, image=btn, bg="#141414")
systemlogo.place(x=170, y=20)

title = Label(origin, text="C R M S", fg="#004FFF", bg="#141414", font=("Valorant", 20))
title.place(x=193, y=160)


#line = Label(origin, text="_______", fg="#004FFF", bg="#141414", font=(20,20,))
#line.place(x=193, y=10, relheight=0.0)

dot1 = Image.open("photos/loaddots/4.png")
dot1 = dot1.resize((20,20), Image.LANCZOS)
dot1 = ImageTk.PhotoImage(dot1)

dot2 = Image.open("photos/loaddots/3.png")
dot2 = dot2.resize((20,20), Image.LANCZOS)
dot2 = ImageTk.PhotoImage(dot2)

dot3 = Image.open("photos/loaddots/2.png")
dot3 = dot3.resize((20,20), Image.LANCZOS)
dot3 = ImageTk.PhotoImage(dot3)

dot4 = Image.open("photos/loaddots/1.png")
dot4 = dot4.resize((20,20), Image.LANCZOS)
dot4 = ImageTk.PhotoImage(dot4)


dotmate1 = Label(origin, image=dot1, bg="#141414")
dotmate1.place(x=192, y=200)

dotmate2 = Label(origin, image=dot2, bg="#141414")
dotmate2.place(x=222, y=200)

dotmate3 = Label(origin, image=dot3, bg="#141414")
dotmate3.place(x=252, y=200)

dotmate4 = Label(origin, image=dot4, bg="#141414")
dotmate4.place(x=282, y=200)


origin.update_idletasks()
startnotice = Label(origin, text="Starting...", bg="#141414", fg="White", font=((23)))
startnotice.place(x=0, y=275)
time.sleep(0.5)


start = 0
while start < 5:
    dotmate1.config(image=dot4)
    dotmate2.config(image=dot1)
    dotmate3.config(image=dot2)
    dotmate4.config(image=dot3)
    time.sleep(0.5)
    origin.update_idletasks()

    dotmate1.config(image=dot3)
    dotmate2.config(image=dot4)
    dotmate3.config(image=dot1)
    dotmate4.config(image=dot2)
    time.sleep(0.5)
    origin.update_idletasks()

    dotmate1.config(image=dot2)
    dotmate2.config(image=dot3)
    dotmate3.config(image=dot4)
    dotmate4.config(image=dot1)
    time.sleep(0.5)
    origin.update_idletasks()

    dotmate1.config(image=dot1)
    dotmate2.config(image=dot2)
    dotmate3.config(image=dot3)
    dotmate4.config(image=dot4)
    time.sleep(0.5)
    origin.update_idletasks()
    start += 1




origin.withdraw()
LogSign = Toplevel()
LogSign.geometry("1200x700")
#LogSign.overrideredirect(1)
LogSign.config(bg="#141414")


#LOGO
uplogo = Image.open("photos\maininlogo.png")
uplogo = uplogo.resize((50,50), Image.LANCZOS)
uplogo = ImageTk.PhotoImage(uplogo)



upframe = Frame(LogSign, width=1200, height=50, bg="#545454")
upframe.place(x=0, y=0)

mainlogo = Label(upframe, image=uplogo, bg="#545454")
mainlogo.place(x=10, y=0)

uplabel = Label(upframe, text="CRIME RECORD MANAGEMENT SYSTEM", bg="#545454", fg="#D9D9D9",font=("Agency FB", 20, "bold"))
uplabel.place(x=60, y=4)

uplogintbn = MD.CTkButton(upframe, text="LOGIN", width=5,fg_color="#545454",font=("Agency FB", 30, "bold"), command=lambda:slideleft())
uplogintbn.place(relx=0.85, y=4)

upsignupbtn = MD.CTkButton(upframe, text="SIGNUP", width=5,fg_color="#545454",font=("Agency FB", 30, "bold"), command=lambda:slidedown())
upsignupbtn.place(relx=0.92, y=4)


#frame to contain the video
vidframe = Frame(LogSign, width=1200, height=650,bg="#545454")
vidframe.place(x=-4, y=50)

a = Label(vidframe,bg="#545454")
a.pack()

video = tkvideo("intro_vid.mp4", a, loop=True, size=(1209, 650))
video.play()


a = Label(LogSign, text="INDICATOR")
a.place(x=1200, y=500)









x_axis = 1300
login = MD.CTkFrame(LogSign, height=400, width=350, bg_color="#141414",fg_color="#D9D9D9",corner_radius=0)
login.place(x=x_axis, y=70)


a = Label(login, text="USER LOGIN", font=("Cambria", 20), bg="#D9D9D9")
a.place(relx=0.280, rely=0.05)

b = Entry(login, width=37, bd=0, font=("Ariel", 10, "bold"), bg="#D9D9D9")
b.place(relx=0.12, rely=0.3, relheight=0.08)

c = Entry(login, width=37, bd=0, font=("Ariel", 10, "bold"), show="*",bg="#D9D9D9")
c.place(relx=0.12, rely=0.5, relheight=0.08)

"""
#d = ttk.Checkbutton(login, text="Remember me")
#d.place(x=32, y=240)
"""
e = MD.CTkButton(login, text="LOG IN", font=("Corbel", 16,"bold"), width=272, hover_color="Red", fg_color="#61777B",bg_color="White",corner_radius=0,command=lambda:gate())
e.place(relx=0.1, rely=0.7, relheight=0.08)

f = MD.CTkButton(login, text="Cancel", font=("Corbel", 16), width=272, hover_color="Red", bg_color="White",corner_radius=0,command=lambda:slideright())
f.place(relx=0.1, rely=0.8, relheight=0.08)

g = MD.CTkButton(login, text="Forgot password?", font=("Corbel", 10), width=272, hover_color="Red", text_color="Black",fg_color="#D9D9D9",bg_color="#D9D9D9",corner_radius=0)
g.place(relx=0.1, rely=0.9, relheight=0.08)

#g = Label(login, text="Don't have an account? Register", font=("Ariel", 10), bg="White")
#g.place(relx=0.2, rely=0.9)

linesimg = Image.open("photos/linya.PNG")
lineimg = linesimg.resize((270,2), Image.LANCZOS)
lineimg = ImageTk.PhotoImage(lineimg)


ID = Label(login, image=lineimg, bg="Black")
ID.place(relx=0.1, rely=0.375, relheight=0.005)

keycode = Label(login, image=lineimg, bg="Black")
keycode.place(relx=0.1, rely=0.575, relheight=0.005)



#CREATING THE ANIMATION FOR USER ID LABEL
def moveup():
    global ycor
    if ycor != 100:
        ycor -=1
        user.place(x=35, y=ycor)
        if ycor > 100:
            login.after(5, moveup)
        else:
                print("FLOWN")
    


def moveback():
    global ycor
    if ycor != 123:
        ycor += 1
        user.place(x=35, y=ycor)
        if ycor < 123:
            login.after(5, moveback)
        else:
            print("LANDED")

indicator = 0
def animation(event):
    global indicator
    indicator += 1
    if indicator % 2 == 0:
        if len(b.get()) > 0:
            1+1
        else:
            moveback()
    else:
        moveup()

#CREATING ANIMATION FOR PASSCODE LABEL


def go_up():
    global codecor
    if codecor != 180:
        codecor -= 1
        passcode.place(x=35, y=codecor)
        if codecor > 180:
            login.after(5, go_up)
        else:
            print("ON")

def go_down():
    global codecor
    if codecor != 203:
        codecor += 1
        passcode.place(x=35, y=codecor)
        if codecor < 203:
            login.after(5, go_down)
        else:
            print("OFF")

switch = 0
def anotheranimation(event):
    global switch
    switch += 1
    if switch % 2 == 0:
        if len(c.get()) > 0:
            1+1
        else:
            go_down()
    else:
        go_up()




#usecor = 100
ycor = 123
user = Label(login, text="USER ID",font=("Corbel", 13,"bold"), bg="#D9D9D9")
user.place(x=35, y=ycor)

#passcor = 180
codecor = 203
passcode = Label(login, text="PASSCODE",font=("Corbel", 13,"bold"), bg="#D9D9D9")
passcode.place(x=35, y=codecor)

b.bind("<Enter>", animation)
b.bind("<Leave>", animation)

c.bind("<Enter>", anotheranimation)
c.bind("<Leave>", anotheranimation)


#340
#700
#ANIMATE THE FRAME

def slideleft():
    global x_axis
    if x_axis != 820:
        x_axis -= 20
        login.place(x=x_axis, y=70)
        if x_axis > 820:
            LogSign.after(10, slideleft)

def slideright():
    global x_axis
    if x_axis != 1300:
        x_axis += 20
        login.place(x=x_axis, y=70)
        if x_axis < 1300:
            LogSign.after(10, slideright)
#_---------------------------------------------------ABOVE ANIMATION FOR FRAMES----------------------------------------



#--------------------------------------------BELOW ANIMATION FOR SIGNUP PANEL AND WIDGETS------------------------------

negCor=-400
signup = MD.CTkFrame(LogSign, width=650, height=400, bg_color="#141414",fg_color="#D9D9D9",corner_radius=0)
#hide
signup.place(x=500, y=negCor)

#show
#signup.place(x=0, y=negCor)


FRAME = MD.CTkScrollableFrame(signup, width=605, height=350, bg_color="#D9D9D9", fg_color="#D9D9D9",corner_radius=0)
FRAME.place(x=4, y=4)

CANVAS = Canvas(FRAME, width=620, height=600, highlightbackground="#D9D9D9", background="#D9D9D9")
CANVAS.pack(fill=BOTH)











signtitle = Label(CANVAS, text="USER SIGNUP", font=("Cambria", 20), bg="#D9D9D9")
signtitle.place(relx=0.340, rely=0.1)

entry_height = 0.06




#FOR X COORDINATES OF WIDGETS inside the signup panel for easy modification
row1 = 15
row2 = 325


name = Entry(CANVAS, width=37, bd=0, font=("Ariel", 10, "bold"), bg="#D9D9D9")
name.place(x=row1, y=160, relheight=entry_height)

Identification = Entry(CANVAS, width=37, bd=0, font=("Ariel", 10, "bold"), bg="#D9D9D9")
Identification.place(x=row2, y=160, relheight=entry_height)

email = Entry(CANVAS, width=37, bd=0, font=("Ariel", 10, "bold"), bg="#D9D9D9")
email.place(x=row1, y=240, relheight=entry_height)

password = Entry(CANVAS, width=37, bd=0, font=("Ariel", 10, "bold"), bg="#D9D9D9")
password.place(x=row2, y=240, relheight=entry_height)

confirmpassword = Entry(CANVAS, width=37, bd=0, font=("Ariel", 10, "bold"), bg="#D9D9D9")
confirmpassword.place(x=row2, y=320, relheight=entry_height)

phonenumber = Entry(CANVAS, width=37, bd=0, font=("Ariel", 10, "bold"), bg="#D9D9D9")
phonenumber.place(x=row1, y=320, relheight=entry_height)

dateofbirth = Entry(CANVAS, width=37, bd=0, font=("Ariel", 10, "bold"), bg="#D9D9D9")
dateofbirth.place(x=row1, y=400, relheight=entry_height)

zipcode = Entry(CANVAS, width=37, bd=0, font=("Ariel", 10, "bold"), bg="#D9D9D9")
zipcode.place(x=row2, y=400, relheight=entry_height)

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
fullname.place(x=row1, y=firstrow)
line = Label(CANVAS, image=lineimg)
line.place(x=row1-1, y=190)

ID = Label(CANVAS, text="USER ID",font=("Corbel", 13,"bold"), bg="#D9D9D9")
ID.place(x=row2,y=firstrow)
line = Label(CANVAS, image=lineimg)
line.place(x=row2-1, y=190)


mail = Label(CANVAS, text="EMAIL",font=("Corbel", 13,"bold"), bg="#D9D9D9")
mail.place(x=row1,y=secondrow)
line = Label(CANVAS, image=lineimg)
line.place(x=row1-1, y=270)

word = Label(CANVAS, text="PASSWORD",font=("Corbel", 13,"bold"), bg="#D9D9D9")
word.place(x=row2,y=secondrow)
line = Label(CANVAS, image=lineimg)
line.place(x=row2-1, y=270)

conword = Label(CANVAS, text="CONFIRM PASSWORD",font=("Corbel", 13,"bold"), bg="#D9D9D9")
conword.place(x=row2,y=thirdrow)
line = Label(CANVAS, image=lineimg)
line.place(x=row2-1, y=350)

phonenum = Label(CANVAS, text="PHONE NUMBER",font=("Corbel", 13,"bold"), bg="#D9D9D9")
phonenum.place(x=row1,y=thirdrow)
line = Label(CANVAS, image=lineimg)
line.place(x=row1-1, y=350)

bday = Label(CANVAS, text="DATE OF BIRTH",font=("Corbel", 13,"bold"), bg="#D9D9D9")
bday.place(x=row1,y=fourthrow)
line = Label(CANVAS, image=lineimg)
line.place(x=row1-1, y=430)

Zcode = Label(CANVAS, text="ZipCode",font=("Corbel", 13,"bold"), bg="#D9D9D9")
Zcode.place(x=row2,y=fourthrow)
line = Label(CANVAS, image=lineimg)
line.place(x=row2-1, y=430)

#####################################-------------ANIMATING THE LABEL WIDGETS-------------------###########################

#-------------------------------------------------NAME LABEL ANIMATION BELOW-------------------------------------------------
#NAME LABEL
#for label NAME to go up
def nameup():
    global firstrow
    if firstrow != 142:
        firstrow-=1
        fullname.place(x=row1, y=firstrow)
        if firstrow > 142:
            signup.after(10, nameup)

#for label NAME to go down

def namedown():
    global firstrow
    if firstrow != 160:
        firstrow +=1
        fullname.place(x=row1, y=firstrow)
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
        ID.place(x=row2,y=firstrow)
        if firstrow > 142:
            signup.after(10,user_up)
        else:
            print("DAP")


def user_down():
    global firstrow
    if firstrow != 160:
        firstrow += 1
        ID.place(x=row2,y=firstrow)
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
        mail.place(x=row1,y=secondrow)
        if secondrow > 222:
            signup.after(10, mail_up)
#TO GO DOWN
def mail_down():
    global secondrow
    if secondrow != 240:
        secondrow += 1
        mail.place(x=row1,y=secondrow)
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
        word.place(x=row2,y=secondrow)
        if secondrow > 222:
            signup.after(10, pass_up)

#TO GO DOWN
def pass_down():
    global secondrow
    if secondrow != 240:
        secondrow += 1
        word.place(x=row2,y=secondrow)
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
        phonenum.place(x=row1,y=thirdrow)
        if thirdrow > 302:
            signup.after(10, phone_up)
    
#TO GO DOWN
def phone_down():
    global thirdrow
    if thirdrow != 320:
        thirdrow += 1
        phonenum.place(x=row1,y=thirdrow)
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
        conword.place(x=row2,y=thirdrow)
        if thirdrow > 302:
            signup.after(10, confirm_up)

#TO GO DOWN
def confirm_down():
    global thirdrow
    if thirdrow != 320:
        thirdrow += 1
        conword.place(x=row2,y=thirdrow)
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
        bday.place(x=row1,y=fourthrow)
        if fourthrow > 382:
            signup.after(10, date_up)

#TO GO DOWN
def date_down():
    global fourthrow
    if fourthrow != 400:
        fourthrow += 1
        bday.place(x=row1,y=fourthrow)
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
        Zcode.place(x=row2,y=fourthrow)
        if fourthrow > 382:
            signup.after(10, code_up)

def code_down():
    global fourthrow
    if fourthrow != 400:
        fourthrow += 1
        Zcode.place(x=row2,y=fourthrow)
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

#ANIMATE THE FRAME CONTAINER
def slidedown():
    global negCor
    
    if negCor != 60:
        negCor+=20
        signup.place(x=500, y=negCor)
        if negCor  < 60:
            LogSign.after(10, slidedown)

def slideup():
    global negCor
    if negCor != -400:
        negCor -=20
        signup.place(x=500, y=negCor)
        if negCor > -400:
            LogSign.after(10, slideup)


#----------------------------------------ZIPCODE LABEL LABEL ANIMATION ABOVE-------------------------------------------------





#BUTTONS
register = MD.CTkButton(CANVAS, text="REGISTER", font=("Agency FB", 30, "bold"),text_color="Black",fg_color="#61777B",corner_radius=0,command=lambda:put_in_db())
register.place(x=row1, y=450, relwidth=0.41,relheight=entry_height)

cancelregister = MD.CTkButton(CANVAS, text="CANCEL", font=("Agency FB", 30, "bold"),text_color="Black",fg_color="#61777B",corner_radius=0,command=lambda:slideup())
cancelregister.place(x=row2, y=450, relwidth=0.41,relheight=entry_height)








#--------------------------------------------ABOVE ANIMATION FOR SIGNUP PANEL AND WIDGETS------------------------------

#----------------------------------------------------------------MAIN INTERFACE----------------------------------------

def SYSTEM():
    LogSign.withdraw()

    CRMS = Toplevel()
    CRMS.geometry("1200x700")
    CRMS.config(bg="Black")


    CRMS_LOGO = Image.open("photos/LINES.png")
    CRMS_LOGO = CRMS_LOGO.resize((50,50), Image.ADAPTIVE)
    CRMS_LOGO = ImageTk.PhotoImage(CRMS_LOGO)



    system_upframe = Frame(CRMS, width=1200, height=50, bg="#545454")
    system_upframe.place(x=0, y=0)

    system_logo_label = Label(CRMS, image=CRMS_LOGO, bg="#545454")
    system_logo_label.place(x=10, y=0)



    system_uplabel = Label(system_upframe, text="CRIME RECORD MANAGEMENT SYSTEM", bg="#545454", fg="#D9D9D9",font=("Agency FB", 20, "bold"))
    system_uplabel.place(x=60, y=4)



    SEARCH_FRAME = Frame(CRMS, width=30, height=40, highlightbackground="Red", highlightcolor="Red", highlightthickness=2)
    SEARCH_FRAME.place(x=15, y=50)


#----------------------------------------------------------------MAIN INTERFACE----------------------------------------








#-----------------------------------------------------------------FRONT END-------------------------------------------------

#-----------------------------------------------------------------BACK END-------------------------------------------------

#LOADING THE EXCEL IN THE PROGRAM
book = load_workbook("CRMSDB.xlsx")

#ASSIGNING THE SPREADSHEET OF CRMSDB.XLSX
SIGN_UP = book["PENDING SIGNUP"]
LOG_IN = book["CREDENTIALS"]
DATABASE = book["MAIN DATA"]



######################LOGGING IN
def gate():
    user_id = b.get()
    pass_code = c.get()


    if len(user_id) <= 0 or len(pass_code) <= 0:
        messagebox.showerror("FIELD","FILL ALL FIELDS TO LOGIN")
    else:
        found = False
        last_cell = LOG_IN.max_row
        for i in range(2, last_cell+1):
            if LOG_IN["A"+str(i)].value == user_id and LOG_IN["B"+str(i)].value == pass_code:
                found = True
                break
            else:
                found = False

        if found == True:
            #calls the system interface which is inside of function
            SYSTEM()
        else:
            messagebox.showerror("WRONG CREDENTIALS")







######################LOGGING IN

######################SIGNUP

def put_in_db():
    sign_name = name.get()
    sign_user_id = Identification.get()
    sign_email = email.get()
    sign_password = password.get()
    sign_confirm_pass = confirmpassword.get()
    sign_phonenumber = phonenumber.get()
    sign_bday = dateofbirth.get()
    sign_zip = zipcode.get()

    



    if len(sign_name) <= 0 or len(sign_user_id) <= 0 or len(sign_email) <= 0 or len(sign_password) <= 0 or len(sign_confirm_pass) <= 0 or len(sign_bday) <= 0 or len(sign_zip) <= 0:
        messagebox.showerror("404","FILL ALL FIELDS TO PROCEED")

        messagebox.showerror("202","PASSWORD DO NOT MATCH")

    else:
        if sign_password != sign_confirm_pass:
            messagebox.showerror("202","PASSWORD DO NOT MATCH")
        else:
            last_row = str(SIGN_UP.max_row+1)

            all_value = ["#",sign_user_id, sign_password, sign_name,sign_phonenumber, sign_email, sign_bday, sign_zip]
            all_column = ["#","A","B","C","D","E","F","G"]
            for i in range(1,len(all_column)):
                SIGN_UP[all_column[i]+last_row].value = all_value[i]
            
            print("REGISTED")
            messagebox.showinfo("SUCCESS","REGISTERED")

            book.save("CRMSDB.xlsx")




    #if len(sign_name)<=0 and len:



######################SIGNUP






#-----------------------------------------------------------------BACK END-------------------------------------------------



origin.mainloop()