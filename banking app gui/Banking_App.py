import tkinter as tk
from tkinter import messagebox
from tkinter import *
import pickle
import random
import os

database = []

def home(window):
    #exits from the current window and goes back to main page

    window.destroy()
    main_program()

class Bank_account:
    def __init__(self,username,password,account_no):
        #Initiates the class. Stores details of clients

        self.username = username
        self.password = password
        self.account_no = account_no
        self.balance = 0
        self.recent_transaction = {}

    def deposit(self,amount,field):
        #converts amount to integer type if amount is not an empty string (to avoid invalid literal ValueError)

        if amount=="":
            amount = 0
        else:
            amount = int(amount)

        #deletes the value entered in the corresponding field

        field.delete(0,END)

        #adds the specified amount to total balance if amount is greater than zero
        #then calls the modify() function with an id for specifying that the call came from here


        if amount > 0:
            self.balance += amount
            self.recent_transaction['deposit'] = amount
            messagebox.showinfo("Done","Amount of {} deposited.".format(amount))
            modify(self,self.username,id="deposit")

        else:
            messagebox.showinfo("Error","Amount must be higher than zero")

    def withdraw(self,amount,field):
        #converts amount to integer type if amount is not an empty string (to avoid invalid literal ValueError)

        if amount=="":
            amount = 0
        else:
            amount = int(amount)

        #deletes the value entered in the corresponding field

        field.delete(0,END)

        #if requested amount is less than or equal to available balance, make corresponding value changes
        #then calls the modify() function with an id for specifying that the call came from here

        if amount <= self.balance and amount > 0:
            self.balance -= amount
            self.recent_transaction['withdraw'] = amount
            messagebox.showinfo("Result","Amount Rs.{} withdrawn.".format(amount))
            modify(self,self.username,id="withdraw")
        elif amount == 0:
            messagebox.showinfo("Error","Amount must be higher than zero")
        else:
            messagebox.showinfo("Error","Insufficient Balance")

    def return_recent_transaction(self):
        #returns the transaction dictionary value when called (though unneccessary)

        return self.recent_transaction

def modify(user,username,id=0):
    #creates the specified file if it doesnt exists and pickles the current object into the file

    print("Readched modify")
    file = open(username+".txt",'wb')
    pickle.dump(user,file)
    file.close()

    #creates a history file for recording transactions if id doesnt exist.

    file = open(username+"-history.txt",'a')
    file.close()

    #If function is being called from inside deposit method of Bank_account class,
    #then append the transaction made into the history file

    if id == "deposit":
        file = open(username+"-history.txt",'a')
        file.write('Deposited: '+str(user.recent_transaction['deposit'])+"\n")
        file.close()

    # If function is being called from inside withdraw method of Bank_account class,
     #then append the transaction made into the history file

    elif id == "withdraw":
        file = open(username+"-history.txt",'a')
        file.write('Withdrawn: '+str(user.recent_transaction['withdraw'])+"\n")
        file.close()
    print(user)

def MakeNewAccount(username,password):
    #if username and password are not empty strings,then proceed to create new account

    if username!="" and password!="":
        account_no = random.randrange(100000,1000000)

        #Instantiating new Bank_account class object

        user = Bank_account(username,password,account_no)
        all_files = os.listdir()

        #checks whether file with username aldready exists and if it doesnt, then proceed to create new account

        if username+".txt" in all_files:
            messagebox.showinfo("Error","Username Not available")

        #appends current object into a list

        else:
            database.append(user)
            modify(user,username)
            messagebox.showinfo("Finished","Account created successfully \n"+"Your account no: "+str(account_no))

        #clears the values entered in input field

        new_name_entry.delete(0,END)
        new_pass_entry.delete(0,END)

def CheckCredentials(window,username,password,account_no):
    global user
    all_files = os.listdir()

    #checks if account_no is an empty string and assigns it an arbitrary value of 0.
    # this is to avoid error when converting account_no into integer type

    if account_no == "":
        account_no = "0"

    #Checks for the file in list of files and unpickles the object from it

    if username+".txt" in all_files:
        file = open(username+".txt",'rb')
        user = pickle.load(file)
        file.close()
        account_no = int(account_no)

        #Verifies whether credentials are accurate

        if user.username == username and user.password == password and user.account_no == account_no:
            window.destroy()
            profile(username,password,account_no)

        #when Credentials entered dont match the real credentials

        else:
            messagebox.showinfo("Error","Invalid Credentials \n Try again")
            login_name_entry.delete(0,END)
            login_password_entry.delete(0,END)
            login_accno_entry.delete(0,END)

    #When the specified account doesn`t exist

    else:
        messagebox.showinfo("Error","Invalid Credentials \n Try again")
        login_name_entry.delete(0,END)
        login_password_entry.delete(0,END)
        login_accno_entry.delete(0,END)

def profile(username,password,account_no):
    #Enters into user`s profile window with the account details specified as parameters

    profile_window = tk.Tk()
    profile_window.title("Account Creation")
    profile_window.geometry("700x400")

    deposit_img = PhotoImage(file = 'images/deposit.gif')
    deposit_img = deposit_img.subsample(3,3)
    transaction_img = PhotoImage(file = 'images/recent-transactions.gif')
    transaction_img = transaction_img.subsample(2,2)
    withdraw_img = PhotoImage(file = 'images/withdraw.gif')
    withdraw_img = withdraw_img.subsample(4,4)
    balance_img = PhotoImage(file = 'images/account-balance.gif')
    balance_img = balance_img.subsample(5,5)
    logout_img = PhotoImage(file = 'images/logout.gif')
    logout_img = logout_img.subsample(3,3)
    bg_img = PhotoImage(file = 'images/anonymous-bg.gif')

    bg = tk.Label(image=bg_img)
    bg.image = bg_img
    bg.place(x=0,y=0)

    tk.Label(profile_window,text = "Welcome {}".format(username),font=("Ariel Black",15)).pack()
    tk.Label(profile_window,text = "").pack()
    tk.Label(profile_window,text = "").pack()

    #lambda function for making temporary function, which in turn calls the specied funtion as
    #tkinter 'command = function' doesnt allow parameters to be passed

    deposit_button = tk.Button(profile_window,image = deposit_img, command = lambda: deposit(profile_window,user))
    deposit_button.image = deposit_img
    deposit_button.place(x=10,y=100)

    withdraw_button = tk.Button(profile_window,image = withdraw_img, command = lambda: withdraw(profile_window,user))
    withdraw_button.image = withdraw_img
    withdraw_button.place(x=360,y=100)

    display_balance_button = tk.Button(profile_window,image = balance_img,command = lambda: ShowBalance(profile_window,user))
    display_balance_button.image = balance_img
    display_balance_button.place(x=10,y=250)

    recent_transaction_button = tk.Button(profile_window,image = transaction_img,command = lambda: recent_transaction(profile_window,user))
    recent_transaction_button.image = transaction_img
    recent_transaction_button.place(x=360,y=250)

    logout_button = tk.Button(profile_window,image = logout_img,command = lambda: home(profile_window))
    logout_button.image = logout_img
    logout_button.place(x=620,y=320)

def deposit(window,user):
    #Opens the amount to be deposited entry field upon being called

    amount = tk.Entry(window)
    amount.place(x=110,y=120)

    text1 = tk.Label(window,text="Enter amount to be deposited",font=("Ariel Black",13))
    text1.place(x=110,y=90)


    submit = tk.Button(window,text = "Submit",width=10,height=1,command = lambda: user.deposit(amount.get(),amount))
    submit.place(x=110,y=140)


def withdraw(window,user):
    #Opens the amount to be withdrawn entry field upon being called
    amount = tk.Entry(window)
    amount.place(x=490,y=120)

    text1 = tk.Label(window,text="Enter amount to be withdrawn",font=("Ariel Black",13))
    text1.place(x=490,y=90)

    submit = tk.Button(window,text = "Submit",width=10,height=1,command = lambda: user.withdraw(amount.get(),amount))
    submit.place(x=490,y=140)


def ShowBalance(window,user):
    #displays current balance available in current window

    show_balance = tk.Label(window,text = "Current balance: {}".format(user.balance),width=30,font=("Ariel Black",15),anchor = 'w')
    show_balance.place(x=10,y=320)

def recent_transaction(window,user):
    #calls the return_recent_transaction method of Bank_account class

    recent = user.return_recent_transaction()
    history = ""

    #opens file containing current users transaction details in order to display it

    file = open(user.username+"-history.txt",'rt')
    for i in file:
        history += i+"\n"
    file.close()
    messagebox.showinfo("History",history)

def create(root):
    #window for account creation

    global new_name_entry,new_pass_entry

    root.destroy()

    creation_window = tk.Tk()
    creation_window.title("Account Creation")
    creation_window.geometry("600x400")

    submit_img = PhotoImage(file = 'images/submit.gif')
    submit_img = submit_img.subsample(1,1)
    home_img = PhotoImage(file = 'images/home.gif')
    home_img = home_img.subsample(2,2)
    bg_img = PhotoImage(file = 'images/anonymous-bg.gif')

    bg = tk.Label(image=bg_img)
    bg.image = bg_img
    bg.place(x=0,y=0)

    tk.Label(creation_window,text="Enter your details below",font=("Ariel Black",15)).pack()
    tk.Label(creation_window,text="").pack()
    tk.Label(creation_window,text="Enter your fullname.",font=("Ariel Black",15)).pack()

    new_name_entry = tk.Entry(creation_window)
    new_name_entry.pack()
    new_name_entry.focus()

    tk.Label(creation_window,text="Create new password.",font=("Ariel Black",15)).pack()

    new_pass_entry = tk.Entry(creation_window,show="*")
    new_pass_entry.pack()

    tk.Label(creation_window,text="").pack()

    submit_button = tk.Button(creation_window,image = submit_img,command =lambda:MakeNewAccount(new_name_entry.get(),new_pass_entry.get()))
    submit_button.image = submit_img
    submit_button.pack()

    tk.Label(creation_window,text="").pack()
    tk.Label(creation_window,text="").pack()
    tk.Label(creation_window,text="").pack()

    back_button = tk.Button(creation_window,image=home_img,command=lambda: home(creation_window))
    back_button.image = home_img
    back_button.pack()

def login(root):
    #window for logging in

    global login_name_entry,login_password_entry,login_accno_entry

    root.destroy()

    login_window = tk.Tk()
    login_window.title("Login")
    login_window.geometry("600x400")

    login_img = PhotoImage(file = 'images/login.gif')
    login_img = login_img.subsample(6,6)
    home_img = PhotoImage(file = 'images/home.gif')
    home_img = home_img.subsample(2,2)
    bg_img = PhotoImage(file = 'images/anonymous-bg.gif')

    bg = tk.Label(image=bg_img)
    bg.image = bg_img
    bg.place(x=0,y=0)

    tk.Label(login_window,text="").pack()
    tk.Label(login_window,text="Enter username",font=("Ariel Black",15)).pack()

    login_name_entry = tk.Entry(login_window)
    login_name_entry.pack()

    tk.Label(login_window,text="Enter account number",font=("Ariel Black",15)).pack()

    login_accno_entry = tk.Entry(login_window)
    login_accno_entry.pack()

    tk.Label(login_window,text="Enter password",font=("Ariel Black",15)).pack()

    login_password_entry = tk.Entry(login_window,show="*")
    login_password_entry.pack()

    tk.Label(login_window,text="").pack()

    submit_button = tk.Button(login_window,image = login_img,command =lambda:CheckCredentials(login_window,login_name_entry.get(),login_password_entry.get(),login_accno_entry.get()))
    submit_button.image = login_img
    submit_button.pack()

    tk.Label(login_window,text="").pack()
    tk.Label(login_window,text="").pack()
    tk.Label(login_window,text="").pack()

    back_button = tk.Button(login_window,image = home_img,command=lambda: home(login_window))
    back_button.image = home_img
    back_button.pack()

def main_program():
    #main window which opens when program is run

    root = tk.Tk()
    root.title("Banking Application")
    root.geometry("700x400")

    create_account_img = PhotoImage(file = 'images/create account.gif')
    create_account_img = create_account_img.subsample(1,1)
    signin_img = PhotoImage(file = 'images/signin.gif')
    signin_img = signin_img.subsample(1,1)
    bg_img = PhotoImage(file = 'images/anonymous-bg.gif')

    a=tk.Label(image=bg_img).place(x=0,y=0)

    tk.Label(root,text="Anonymous Bank",font=("Ariel Black",60),bg=a,fg='blue').pack()

    create_button = tk.Button(root,image = create_account_img,command = lambda:create(root))
    create_button.image = create_account_img
    create_button.place(x=250,y=100)

    signin_button = tk.Button(root,image = signin_img,command = lambda:login(root))
    signin_button.image = signin_img
    signin_button.place(x=250,y=200)

    root.mainloop()
main_program()
