import pickle,os
import main,users

#adds a new element to the questions dictionary and pickle it back.
def modify_file(title,question,description):
    with open(f'{main.questions_database}questions','rb') as file:
        main.total_questions = pickle.load(file)
        main.total_questions[title] = [question,description]
    with open(f'{main.questions_database}questions','wb') as file:
        pickle.dump(main.total_questions,file)

def return_questions():
    questions = os.listdir(main.questions_database)
    return questions

#used for the "back" button
def home(window,func):
    window.destroy()
    func()

def MakeNewAccount(new_name_entry,new_pass_entry):
    username = new_name_entry.get()
    password = new_pass_entry.get()

    #creates new user if username is not aldready taken
    if username!="" and password!="":
        if 'Users-Database' in main.current_folder:
            users_database = os.listdir('Users-Database')
            if username+".txt" in users_database:
                main.messagebox.showinfo("Error","Username aldready taken!")

            else:
                user = users.Person(username,password)
                user.modify()
                main.messagebox.showinfo("Finished","Account Has Been Created!")

                new_name_entry.delete(0,main.END)
                new_pass_entry.delete(0,main.END)
def CheckCredentials(window,username,password):
    #To verify user and proceed to enter profile window
    global user
    all_files = os.listdir(f'{main.current_path}\\Users-Database')
    if f'{username}.txt' in all_files:
        with open(f'{main.current_path}\\Users-Database\\{username}.txt','rb') as file:
            user = pickle.load(file)
        if user.authenticate(username,password):
            main.Profile(user,window)
        else:
            main.messagebox.showinfo("Error","Invalid Credentials \n Try again")
    else:
        main.messagebox.showinfo("Error","Invalid Credentials \n Try again")

def CheckSolution(window,title,answer):
    #creates a .py file containing candidates solution
    with open(f'{main.answers_database}{title}.py','wt') as file:
        file.write(f'{answer}')

    #runs the candidate solution with original corresponding input file
    #and stores its output to a file and error to different file(if any)
    os.system(f'python "{main.answers_database}{title}.py" < "{main.questions_database}{title}\\input.txt" > "{main.answers_database}{title}--output.txt"  2> "{main.answers_database}{title}--output_err.txt"')

    with open(f'{main.answers_database}{title}--output_err.txt','r') as file:
        error_text = file.read()

    #evaluates the code by
    #comparing the original output to candidates output file
    if error_text=="":
        with open(f'{main.answers_database}{title}--output.txt','r') as file:
            solver_output = file.read()

        with open(f'{main.questions_database}{title}\\output.txt','r') as file:
            setter_output = file.read()

        if setter_output==solver_output:
            main.messagebox.showinfo('Result','Your answer is correct',parent=window)
        else:
            main.messagebox.showinfo('Result','Wrong answer',parent=window)

    else:
        main.messagebox.showinfo('Error',f'{error_text}',parent=window)

    #deletes the candidate`s files which were generated
    os.remove(f'{main.answers_database}{title}.py')
    os.remove(f'{main.answers_database}{title}--output.txt')
    os.remove(f'{main.answers_database}{title}--output_err.txt')
