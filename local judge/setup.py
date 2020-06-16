import os,pickle

current_path = os.path.dirname(__file__)

# Makes the required directories if it doesnt exist
try: os.mkdir(f'{current_path}\\Questions-Database')
except: pass
try: os.mkdir(f'{current_path}\\Temp-Ans-Storage')
except: pass
try: os.mkdir(f'{current_path}\\Users-Database')
except: pass
##############################################

current_folder = os.listdir()
questions_database = f'{current_path}\\Questions-Database\\'
answers_database = f'{current_path}\\Temp-Ans-Storage\\'
total_questions = {}
bg = 'cadet blue'


#makes a 'questions' file if it doesnt exist
#and pickles an empty dictionary into it(to avoid a certain EOF error)
try:
    with open(f'{questions_database}questions','rb') as file:
        pass
except FileNotFoundError:
    with open(f'{questions_database}questions','wb') as file:
        pickle.dump(total_questions,file)
#############################################################

