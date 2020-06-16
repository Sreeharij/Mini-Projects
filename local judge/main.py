import tkinter as tk
from tkinter import *
from tkinter import messagebox
import pickle,random,os
import tkinter.scrolledtext as tkst
import shutil
import support as sp
import users
import questions as qt

current_path = os.path.dirname(__file__)
current_folder = os.listdir()
questions_database = f'{current_path}\\Questions-Database\\'
answers_database = f'{current_path}\\Temp-Ans-Storage\\'
total_questions = {}
bg = 'cadet blue'


def login(root):
    #window for logging in

    root.destroy()

    global login_name_entry,login_password_entry

    login_window = tk.Tk()
    login_window.title("Login")
    login_window.geometry("700x400")
    login_window.config(bg='cadet blue')

    tk.Label(login_window,text="",bg='cadet blue').pack()
    tk.Label(login_window,text="Enter username",bg='powder blue',relief=RIDGE,font=("Ariel Black",17)).pack()

    login_name_entry = tk.Entry(login_window)
    login_name_entry.pack()
    login_name_entry.focus()

    tk.Label(login_window,text="",bg='cadet blue').pack()

    tk.Label(login_window,text="Enter Password",bg='powder blue',relief=RIDGE,font=("Ariel Black",17)).pack()

    login_password_entry = tk.Entry(login_window,show="*")
    login_password_entry.pack()
    tk.Label(login_window,text="",bg='cadet blue').pack()

    submit_button = tk.Button(login_window,text="Login",font=("Ariel",13),bg='powder blue',width=20,height=2,command =lambda:sp.CheckCredentials(login_window,login_name_entry.get(),login_password_entry.get()))
    submit_button.pack()

    tk.Label(login_window,text="",bg='cadet blue').pack()
    tk.Label(login_window,text="",bg='cadet blue').pack()
    tk.Label(login_window,text="",bg='cadet blue').pack()

    back_button = tk.Button(login_window,text="Back Home",width=20,height=2,bg='powder blue',command=lambda: sp.home(login_window,main))
    back_button.pack()

def create(root):
    global new_name_entry,new_pass_entry

    root.destroy()

    creation_window = tk.Tk()
    creation_window.title("Account Creation")
    creation_window.geometry("700x400")
    creation_window.config(bg='cadet blue')

    tk.Label(creation_window,text="Enter your details below",bg='powder blue',relief=RIDGE,font=("Ariel Black",17)).pack()
    tk.Label(creation_window,text="",bg='cadet blue').pack()
    tk.Label(creation_window,text="Enter your fullname.",bg='powder blue',relief=RIDGE,font=("Ariel Black",17)).pack()

    new_name_entry = tk.Entry(creation_window,width=30)
    new_name_entry.pack()
    new_name_entry.focus()

    tk.Label(creation_window,text="",bg='cadet blue').pack()

    tk.Label(creation_window,text="Create new password.",bg='powder blue',relief=RIDGE,font=("Ariel Black",17)).pack()

    new_pass_entry = tk.Entry(creation_window,show="*",width=30)
    new_pass_entry.pack()

    tk.Label(creation_window,text="",bg='cadet blue').pack()

    submit_button = tk.Button(creation_window,text="Submit",font=("Ariel",13),bg='powder blue',width=20,height=2,command =lambda:sp.MakeNewAccount(new_name_entry,new_pass_entry))
    submit_button.pack()

    tk.Label(creation_window,text="",bg='cadet blue').pack()
    tk.Label(creation_window,text="",bg='cadet blue').pack()
    tk.Label(creation_window,text="",bg='cadet blue').pack()

    back_button = tk.Button(creation_window,text="Back Home",width=20,height=2,bg='powder blue',command=lambda: sp.home(creation_window,main))
    back_button.pack()


def Profile(user,window):
    #window for profiles

    window.destroy()
    profile_window = tk.Tk()
    profile_window.geometry("800x500")
    profile_window.title('Local Judge')
    profile_window.config(bg='cadet blue')

    questions = sp.return_questions()
    row = 10

    for i in range(len(questions)):
        if questions[i]=='questions':
            continue


        #helper function to create individual scope for many labels which are using .bind() method
        def make_lambda(title):
            return lambda some_var: solve_q(title)

        row += 50
        question = Label(profile_window,text=str(i+1)+")"+questions[i],font=('Ariel Black',20),width=20,foreground="blue",bg="cadet blue",anchor="w")
        question.bind('<Button-1>',make_lambda(questions[i]))
        question.place(x=50,y=row)

    upload_q_button = tk.Button(profile_window,text="Upload Your Question",height=2,font=("Ariel",13),bg='powder blue',command = lambda:upload_q(user,profile_window))
    upload_q_button.place(x=600,y=10)

    Refresh = tk.Button(profile_window,text="Refresh",height=2,font=("Ariel",13),bg="powder blue",command =lambda: Profile(user,profile_window))
    Refresh.place(x=550,y=400)


def upload_q(user,window):
    #window for uploading questions

    window.destroy()

    upload_q_window = tk.Tk()
    upload_q_window.title('Upload Question')
    upload_q_window.geometry('700x500')
    upload_q_window.config(bg=bg)

    Label(upload_q_window,text="Enter Question:",font=("Ariel black",16),bg=bg).grid()
    question = tkst.ScrolledText(upload_q_window,width=35,height=5)
    question.place(x=0,y=30)

    Label(upload_q_window,text="Give Description(optional):",font=("Ariel black",16),bg=bg).place(x=0,y=120)
    description = tkst.ScrolledText(upload_q_window,width=35,height=10)
    description.place(x=0,y=160)

    Label(upload_q_window,text="Provide input if neccessary",font=("Ariel black",16),bg=bg).place(x=0,y=330)
    input_area = tkst.ScrolledText(upload_q_window,width=35,height=5)
    input_area.place(x=0,y=360)

    back_button = tk.Button(upload_q_window,text="Back Home",width=20,height=2,bg='powder blue',command=lambda: Profile(user,upload_q_window))
    back_button.place(x=0,y=450)

    Label(upload_q_window,text="Provide Solution",font=("Ariel black",16),bg=bg).place(x=310,y=0)
    solution = tkst.ScrolledText(upload_q_window,width=35,height=25)
    solution.place(x=310,y=30)

    Label(upload_q_window,text="Title: ",font=("Ariel black",16),bg=bg).place(x=310,y=445)
    title_entry = Entry(upload_q_window)
    title_entry.place(x=360,y=450)

    submit_button = Button(upload_q_window,text="Submit",bg="powder blue",width=15,font=("Ariel black",15),command=lambda:qt.Question(user,upload_q_window,question.get('1.0',END),solution.get('1.0',END),description.get('1.0',END),title_entry.get(),input_area.get('1.0',END)))
    submit_button.place(x=500,y=440)



def solve_q(title):
    #window for submitting candidate solutions

    solve_q_window = tk.Tk()
    solve_q_window.title('Upload Question')
    solve_q_window.geometry('700x700')
    solve_q_window.config(bg="cadet blue")

    #unpickles the file containing the dictionary for all questions
    with open(f'{questions_database}questions','rb') as file:
        total_questions = pickle.load(file)

    question,description = total_questions[title]

    q = Label(solve_q_window,text=f"Question: {question}",bg='cadet blue',font=("Ariel",17)).pack()
    d = Label(solve_q_window,text=f"Description:\n{description}",bg='cadet blue',font=("Ariel",13),anchor="w").pack()

    sol_entry = tkst.ScrolledText(solve_q_window,width=80,height=20)
    sol_entry.pack()

    submit_button = Button(solve_q_window,text="Submit",bg="powder blue",width=15,font=("Ariel black",15),command=lambda: sp.CheckSolution(solve_q_window,title,sol_entry.get('1.0',END)))
    submit_button.pack()

def main():
    #main window

    root = tk.Tk()
    root.title("Local Judge App")
    root.geometry("700x400")
    root.config(bg='cadet blue')

    #creates a guest Person object in case user Logs In as guest
    guest = users.Person('Guest','123')

    create_button = tk.Button(root,text="Create Account",width=20,height=2,font=("Ariel",17),bg='powder blue',command = lambda:create(root)).place(x=230,y=50)

    login_button = tk.Button(root,text="Login",width=20,height=2,font=("Ariel",17),bg='powder blue',command = lambda:login(root)).place(x=230,y=150)

    guest_button = tk.Button(root,text="Login as guest",width=20,height=2,font=("Ariel",17),bg='powder blue',command =lambda: Profile(guest,root)).place(x=230,y=250)

    root.mainloop()

if __name__=='__main__':
    main()
