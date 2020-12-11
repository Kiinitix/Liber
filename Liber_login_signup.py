#importing libraries

from tkinter import *
from tkinter.messagebox import showerror, showinfo
import mysql.connector as sqltor
from PIL import ImageTk,Image


#Setting up the GUI window
win = Tk()
win.title("Liber")
win.geometry('420x300')
win.resizable(0,0)

#login page background
C = Canvas(win, bg="blue", height=250, width=300)
filename = PhotoImage(file = "C:\\Users\\KABIR\\Desktop\\DSC\\backgroundDefault.png")
background_label = Label(win, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


#dialogue box for sucessful registration and error
def info():
    showinfo("Success!", "Yes you can sign in! ")
def showerror():
    showerror("ERROR!","User already exist, try sign in")


#setting up connection
mycon=sqltor.connect(host="localhost", user="root", passwd="1234", database="root")
if mycon.is_connected()==False:
    print("ERROR connecting to MySQL database!")

#creating cursor
cursor=mycon.cursor()


#Creating the widgets
Label(win, 
         text="USERNAME").grid(row=1, column=3)
Label(win, 
         text="PASSWORD").grid(row=3, column=3)


e1 = Entry(win)
e2 = Entry(win)


e1.grid(row=1, column=6)
e2.grid(row=3, column=6)

username= e1.get()
password= e2.get()

#adding buttons

button = Button(win, text="SIGN IN", width=20)
button1 = Button(win, text="SIGN UP", width=20)
button2 = Button(win, text="EXIT", width=10)

#Positioning the widgets

button.grid(row=6, column=6, columnspan=2, pady=5)
button1.grid(row=7, column=6, columnspan=2, pady=5)
button2.grid(row=20, column=7, columnspan=1, pady=3)

#function to signin
def sign_in():
    global username
    global password
    command=("select username, password from liber where username=%s and password=%s")
    while command:
        info()
        break



#function to singup           
def sign_up():
    win = Tk()
    win.title("Sign up")
    win.geometry('420x300')
    cursor.execute("use root;")
    l1 = Label(win, text="USERNAME")
    entry = Text(win, width=50, height=2, wrap=WORD)
    l2 = Label(win, text="PASSWORD")
    output = Text(win, width=50, height=2, wrap=WORD)


    Label(win, 
             text="USERNAME").grid(row=0)
    Label(win, 
             text="PASSWORD").grid(row=1)


    usrname = Entry(win)
    pssword = Entry(win)


    usrname.grid(row=0, column=1)
    pssword.grid(row=1, column=1)


    A= usrname.get()
    B= pssword.get()
    def enter():
        cursor.execute("use root;")
        cursor.execute("INSERT INTO User(username, password) VALUES ('%s',%s)" % (A,B))
    

    button = Button(win, text="REGISTER", width=20)
    button.grid(row=6, column=6, columnspan=2, pady=5)

    button1 = Button(win, text="EXIT", width=10)
    button1.grid(row=7, column=6, columnspan=2, pady=5)


    button.configure(command=enter)


    def quit_():
        win.destroy()
    button1.configure(command=quit_)
    
#quit button   
def quit_():
    win.destroy()
    
#Button activation
button.configure(command=sign_in)
button1.configure(command=sign_up)
button2.configure(command=quit_)


#So the program is on repeat
win.mainloop()
