from tkinter.messagebox import showerror, showinfo
import tkinter as tk 
import mysql.connector  
from tkinter import *
import mysql.connector as sqltor
from PIL import ImageTk,Image
import SignUp

root = tk.Tk() 
root.geometry("300x300") 
root.title("Login Page")
root.resizable(0,0)

mycon=sqltor.connect(host="localhost", user="<user-name>", passwd="<password>", database="<database-name>")
if mycon.is_connected()==False:
    print("ERROR connecting to MySQL database!")

#creating cursor
cursor=mycon.cursor() 

C = Canvas(root, bg="blue", height=250, width=300)
filename = PhotoImage(file = "C:\\Users\\KABIR\\Desktop\\DSC_Liber\\backgroundDefault.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

def quit_():
        root.destroy()
  
def info():
    showinfo("Success!", "Yes you can sign in! ")
def showerror():
    showerror("ERROR!","User already exist, try sign in")
    
def submitact(): 
      
    user = Username.get() 
    passw = password.get()
    cursor.execute("use root;")
    cursor.execute("select * from liber where username = '%s' and password = %s;" %(user,str(passw)))
    data1=cursor.rowcount
    print(data1)
    if (data1==1):
        root=tk.Tk()
        root.geometry('300x300')
        root.title("sucess")

    else:
        root=tk.Tk()
        root.geometry('300x300')
        root.title("failed")

 
# Definging the first row 
lblfrstrow = tk.Label(root, text ="Username -", ) 
lblfrstrow.place(x = 50, y = 20) 
  
Username = tk.Entry(root, width = 35) 
Username.place(x = 150, y = 20, width = 100) 
   
lblsecrow = tk.Label(root, text ="Password -") 
lblsecrow.place(x = 50, y = 50) 
  
password = tk.Entry(root, width = 35) 
password.place(x = 150, y = 50, width = 100) 
  
loginbutton = tk.Button(root, text ="Login", command = submitact) 
loginbutton.place(x = 150, y = 135, width = 55)

signupbutton = tk.Button(root, text ="Sign Up", command = SignUp.sign_up ) 
signupbutton.place(x = 150, y = 175, width = 55)

exitbutton = tk.Button(root, text ="Exit", command = quit_) 
exitbutton.place(x = 150, y = 215, width = 55)
  
root.mainloop() 
