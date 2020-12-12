import mysql.connector
from tkinter import *

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="root"
)
mycursor = mydb.cursor()

def first_window():
    first_window.app0 = Tk()

    first_window.app0.title("Book Service system")

    first_window.app0.geometry("400x400")

    first_window.app0.minsize(400,400)
    
    Label(first_window.app0,text = "Welcome to Library").place(x = 130, y = 100)

    Label(first_window.app0,text = "Chose from the following options").place(x = 100, y = 130)

    Button(first_window.app0, text = "Borrow Book ", command = search_window).place(x = 130, y = 160)

    Button(first_window.app0, text = "Submit Book ", command = submit_window).place(x = 130, y = 190)

def search_window():
    search_window.app = Tk()

    first_window.app0.destroy()

    search_window.app.geometry("400x400")

    search_window.app.minsize(400,400)
    
    search_window.app.title("Book Service system")

    Label(search_window.app,text = "Book Name").place(x = 40, y =100)

    Label(search_window.app,text = "ISBN No.").place(x = 40, y =130)

    search_button = Button(search_window.app,text = "Search",command = lambda:[result_screen()]).place(x = 40, y = 160)

    search_window.e1 = Entry(search_window.app)
    search_window.e2 = Entry(search_window.app)

    search_window.e1.place(x = 130, y = 100)
    search_window.e2.place(x = 130, y = 130)

def submit_window():
            
    def submit():
        bookname = submit_window.e1.get()
        isbn = submit_window.e2.get()

        mycursor.execute("select Quantity from Book_List where bookname = '{}' or ISBN = '{}'".format(bookname,isbn))

        result = str(mycursor.fetchall())

        result1 = int(result[3:-4])

        quantity = (result1 + 1)

        mycursor.execute("UPDATE Book_List SET Quantity = '{}' where bookname = '{}' or ISBN = '{}'".format(quantity,bookname,isbn))
        mydb.commit()

        mycursor.execute("select Quantity from Book_List where bookname = '{}' or ISBN = '{}'".format(bookname,isbn))

        result = str(mycursor.fetchall())
        
        result2 = int(result[3:-4])

        if(result2>result1):
            Label(submit_window.app2,text = "Book Submitted!").place(x = 40 , y = 190)
        else:
            Label(submit_window.app2,text = "Try Again!").place(x = 40 , y = 190)

    submit_window.app2 = Tk()

    first_window.app0.destroy()

    submit_window.app2.geometry("400x400")

    submit_window.app2.minsize(400,400)
    
    submit_window.app2.title("Book Service system")

    Label(submit_window.app2,text = "Book Name").place(x = 40, y =100)

    Label(submit_window.app2,text = "ISBN No.").place(x = 40, y =130)

    submit_window.e1 = Entry(submit_window.app2)
    submit_window.e2 = Entry(submit_window.app2)

    submit_window.e1.place(x = 130, y = 100)
    submit_window.e2.place(x = 130, y = 130)

    
    Button(submit_window.app2,text = "Submit",command = submit).place(x = 40, y = 160)


def result_screen():
    app1 = Tk()

    app1.title("Book Service System")

    app1.geometry("400x400")

    app1.minsize(400,400)

    bookname = str(search_window.e1.get())

    isbn = str(search_window.e2.get())

    search_window.app.destroy()

    mycursor.execute("select bookname from Book_List where bookname = '{}' or ISBN = '{}'".format(bookname,isbn))

    result = str(mycursor.fetchall())
    
    Label(app1,text = result[3:-4]).place(x = 100 , y = 100)

    mycursor.execute("select ISBN from Book_List where bookname = '{}' or ISBN = '{}'".format(bookname,isbn))

    result = str(mycursor.fetchall())

    Label(app1,text = result[3:-4]).place(x = 100 , y = 130)

    mycursor.execute("select Quantity from Book_List where bookname = '{}' or '{}'".format(bookname,isbn))

    result = str(mycursor.fetchall())

    result1 = int(result[3:-4])

    quantity = (result1 - 1)

    if(result1>0):
        Label(app1,text = "Availabe").place(x = 100, y = 160)
    else:
        Label(app1,text = "Not Availabe").place(x = 100, y = 160)

    mycursor.execute("UPDATE Book_List SET Quantity = '{}' where bookname = '{}' or ISBN = '{}'".format(quantity,bookname,isbn))

    mydb.commit()


first_window()    

