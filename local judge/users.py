import os,pickle
current_path = os.path.dirname(__file__)

class Person:
    def __init__(self,username,password):
        self.username = username.replace(' ','_')
        self.password = password
        self.questions_uploaded = {}
        self.questions_solved = {}

    def authenticate(self,username,password):
        if self.username == username and self.password == password:
            return True

    #pickles the new user object into the corresponding file
    def modify(self):
        with open(f"{current_path}\\Users-Database\\{self.username}.txt",'wb') as file:
            pickle.dump(self,file)

