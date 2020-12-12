import tkinter as tk 
import mysql.connector as sqltor  
from tkinter import * 
from PIL import ImageTk,Image

def sign_up():

    mycon=sqltor.connect(host="localhost", user="root", passwd="1234", database="root")
    if mycon.is_connected()==False:
        print("ERROR connecting to MySQL database!")  

    cursor=mycon.cursor()

    def insert_db(): 
        cursor.execute("use root;")
        user = Username.get() 
        passw = password.get() 
   
        sql = "INSERT INTO Liber (username, password) VALUES (%s, %s)"
        val = (user, passw)
        cursor.execute(sql, val) 
        mycon.commit()

    
    def quit_():
        root.destroy()


    root = tk.Tk() 
    root.geometry("300x300") 
    root.title("Sign up")  
    root.resizable(0,0)


    # Definging the first row 
    lblfrstrow = tk.Label(root, text ="Username -", ) 
    lblfrstrow.place(x = 50, y = 20) 
  
    Username = tk.Entry(root, width = 35) 
    Username.place(x = 150, y = 20, width = 100) 
   
    lblsecrow = tk.Label(root, text ="Password -") 
    lblsecrow.place(x = 50, y = 50) 
  
    password = tk.Entry(root, width = 35) 
    password.place(x = 150, y = 50, width = 100) 
  
    sign_upbutton = tk.Button(root, text ="Sign Up", command = insert_db) 
    sign_upbutton.place(x = 150, y = 135, width = 55)

    exitbutton = tk.Button(root, text ="exit", command = quit_) 
    exitbutton.place(x = 150, y = 185, width = 55)
  
    root.mainloop() 
