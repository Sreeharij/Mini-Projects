import pickle,os,sys

def set_question(author_name):
    question = input('\nEnter the question: ')
    num = int(input("Enter number of options: "))
    question_object = {'question':question,
                        'author':author_name,
                        }
    for i in range(1,num+1):
        option = input(f"Enter option{i}: ")
        question_object[f'option{i}'] = [option,0]
    with open('questions.dat','ab') as f:
        pickle.dump(question_object,f)
    print("Question set Successfully!. ")

    c = input('Exit? (y,n)')
    os.system('cls')
    if c=='y':
        sys.exit()
    else:
        main()

def get_questions():
    all_questions = []
    try:
        with open('questions.dat','rb') as f:
            while True:
                all_questions.append(pickle.load(f))
    except:
        pass
    return all_questions

def cast_vote(cnt,all_questions,question_number):
    vote = int(input("\nEnter option number to vote(1,2,3,4..): "))

    if vote<=cnt:
        all_questions[question_number][f'option{vote}'][1] += 1
        print('Vote Casted!')
        print("\nResult:\n")
        for item in all_questions[question_number]:
            if item!='question' and item!='author':
                current_option = all_questions[question_number][item][0].capitalize()
                option_votes = all_questions[question_number][item][1]
                print(current_option+': ',option_votes)

        with open('questions.dat','wb') as f:
            for item in all_questions:
                pickle.dump(item,f)
    else:
        print("Invalid choice.")
        cast_vote(cnt,all_questions,question_number)

    c = input('Exit? (y,n)')
    os.system('cls')
    if c=='y':
        sys.exit()
    else:
        main()

def main():
    print("\nWELCOME TO ONLINE POLLING BOOTH!\n")
    user_type = input(f"Are you a voter or a question setter?(v,q): ")
    os.system('cls')

    if user_type == 'q':
        name = input("Enter your name to proceed: ")
        set_question(name)

    elif user_type == 'v':
        all_questions = get_questions()
        print("\nAvailable questions:\n")
        total_questions = 0
        for i in range(len(all_questions)):
            total_questions += 1
            print(f"{i+1} {all_questions[i]['question']}")
        question_number = int(input("\nEnter question number to answer: ")) - 1
        while question_number >= total_questions:
            print("Invalid input. ")
            question_number = int(input("\nEnter question number to answer: ")) - 1
        else:
            os.system('cls')
            cnt = 0
            print(f"Question: {all_questions[question_number]['question']}\n")
            for key in all_questions[question_number]:
                if key!='question' and key!='author':
                    cnt += 1
                    print(key.capitalize()+': ', all_questions[question_number][key][0])
            print(f"\nAuthor: {all_questions[question_number]['author']}\n")

            cast_vote(cnt,all_questions,question_number)
    else:
        print("Invalid input. ")
main()
