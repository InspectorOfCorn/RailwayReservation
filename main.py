

import tkinter as tk
import sys
from tkinter import messagebox
from PIL import ImageTk
root = tk.Tk()
root.geometry("1366x720")
root.title("VTA Railway Ticket System")

user_value = tk.StringVar()
pass_value = tk.StringVar()

counter = 0

def login1():
    if user_value.get() == "" or pass_value.get() == "":
        messagebox.showerror("Error","All fields are required", parent=root)
        sys.exit()
    
    
    import mysql.connector as con
    connection = con.connect(host="localhost", user="root", password="OgKepler", database = "VTA")
#Main Method for the login page
    cursor = connection.cursor()
    
    cursor.execute("select count() from data")
    afetch = cursor.fetchone()
    bfetch = afetch[0] # number of rows
    
    username = user_value.get()
    password = pass_value.get()
    
    cursor.execute("select username,password from data where username=username and password=password")
    row = cursor.fetchall()
    
    global counter
    
    for i in range(0,bfetch):
        if(row[i][0] == username and row[i][1]==password):
            counter=1
    if counter == 1:
        messagebox.showinfo("Found","Logging in")
        messagebox.showinfo("Hello","Please close this window to continue")
        print("found")
        
    else:
        messagebox.showinfo("Not found", "password and uservalue does not match")
    
    connection.close()
    
    
    
    
def signup1():
    print("Hi")
def main(): 
    img = ImageTk.PhotoImage(file="background.png")
    background_label = tk.Label(root, image=img)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    global user_value
    global pass_value

    frame_input = tk.Frame(root, bg='#f48d51')
    frame_input.place(x=320,y=130,height=500,width=400)
    #.place will place at desired locaitons
    
    #Adding Labels to the frame
    
    login = tk.Label(text="LOGIN", font=("Helvetica bold",24),).place(x=400, y=150)
    
    user_label = tk.Label(text="USERNAME", font=("Helvetica", 25), fg="orangered",borderwidth=4, relief=tk.RIDGE).place(x=340,y=230)
    pass_label = tk.Label(text="PASSWORD", font=("Helvetica", 24), fg="orangered",borderwidth=4, relief=tk.RIDGE).place(x=340,y=340)
    
    
    #Creating entry widgets
    user_entry = tk.Entry(root, fg="red",bg="darkgray", textvariable=user_value)
    password_entry = tk.Entry(root,fg="red",bg="darkgray", textvariable=pass_value)
    user_entry.place(x= 340,y=280)
    password_entry.place(x=340,y=390)
    
    #login button
    
    btn1 = tk.Button(frame_input, text="Login",font=("Century Gothic",22),bg="orangered", fg="white", command=login1)
    btn1.place(x=90,y=340)
    
    # if not logged i nalready
    
    btn2 = tk.Button(frame_input, text="Not registered? \n Sign up", font=("Century Gothic",16),
                     bg="orangered",fg="white", command=signup1)
    btn2.place(x=70,y=420)
    
    
    
    
    
    root.mainloop()
    
main()
    