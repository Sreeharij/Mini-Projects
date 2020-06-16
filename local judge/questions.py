import os,main
import support as sp

class Question:
    def __init__(self,user,window,question,answer,description,title,input):
        title = title.replace(' ','-')

        #keeps track of how many untitled problems are submitted
        #and assigns a title accordingly
        if title == "":
            count=0
            for file in os.listdir(main.questions_database):
                if 'blank' in file:
                    count+=1
            title = f'blank{count}'

        number = len(os.listdir(main.questions_database))

        try:
            os.mkdir(f'{main.questions_database}{title}')
            self.question = question
            self.answer = answer
            self.description = description
            self.input = input
            self.title = title
            self.user = user
            self.username = user.username

            user.questions_uploaded[self.title] = self.question

            #creates the corresponding files when question is submitted
            #runs the .py file with input file and collects output in another file
            with open(f'{main.questions_database}{self.title}\\question.txt','w') as file:
                file.write(f'Question: {self.question} \nDescription: {self.description}')
            with open(f'{main.questions_database}{self.title}\\answer.txt','w') as file:
                file.write(f'Solution: \n{self.answer} \n\n\n\nAuthor: {self.username}')
            with open(f'{main.questions_database}{self.title}\\input.txt','w') as file:
                file.write(f'{self.input}')
            with open(f'{main.questions_database}{self.title}\\{self.title}.py','w') as file:
                file.write(f'{self.answer}')
            os.system(f'python "{main.questions_database}{self.title}\\{self.title}.py" < "{main.questions_database}{self.title}\\input.txt" > "{main.questions_database}{self.title}\\output.txt" 2> "{main.questions_database}{self.title}\\output_err.txt"')

            with open(f'{main.questions_database}{self.title}\\output_err.txt','rt') as file:
                error_text = file.read()

            if error_text == "":
                with open(f'{main.questions_database}{self.title}\\output.txt','r') as file:
                    output_text = file.read()

                main.messagebox.showinfo("Finished",f"Output:\n{output_text}")

                #calls the function to store the changes to a file
                sp.modify_file(title,question,description)

                #reloads the profile window
                main.Profile(user,window)

            #deletes the generated directory if error exist
            else:
                main.messagebox.showinfo("Error",f"{error_text}")
                main.shutil.rmtree(f'{main.questions_database}{title}')


        except FileExistsError:
            main.messagebox.showinfo("Error","File Already Exist")
