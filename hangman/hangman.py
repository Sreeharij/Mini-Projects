import random,os,man
vowels = 'AEIOUaeiou'
alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
def print_man(key):
    body = {6:'',5:man.head,4:man.trunk,3:man.left_arm,2:man.right_arm,1:man.left_leg,0:man.right_leg}
    print(f"\t\t\t\t\t\t {body[key]}")
def new_movie():
    file = open('movies.txt','rt')
    number = random.randint(1,490)
    i=1
    for line in file:
        i+=1
        if i==number:
            movie = line
            break
        else:
            continue
    file.close()
    return movie

def str_format(original_string):
    global original_list,new_list
    original_list = [i for i in original_string]
    new_list =[]
    for i in range(0,len(original_list)-1):
        if original_list[i] == ' ':
            new_list.append('/')
        elif original_list[i] not in alphabets:
            new_list.append(original_list[i])
        elif original_list[i] not in vowels:
            new_list.append('_')
        elif original_list[i] in vowels:
            new_list.append(original_list[i])
def main():
    global original_string
    original_string = new_movie()
    str_format(original_string)
    for letter in new_list:
        print(letter,end="")
    print()
    print("\t\t\t Lives remaining:",lives)
    while '_' in new_list:
        if lives == 0:
            print("Game over")
            print("Answer: ",end="")
            for letter in original_string:
                print(letter,end="")
            break
        letter = input("\nEnter letter: ")
        update(new_list,letter)
    else:
        print("You won! \nGame Over")

def update(new_list,letter):
    global lives
    if (letter.upper() not in original_string) and (letter.lower() not in original_string):
        if (letter.upper() not in temp) and (letter.lower() not in temp):
            if (letter.upper() not in vowels) and (letter.lower() not in vowels):
                temp.append(letter)
                lives -= 1
    for i in range(0,len(original_list)-1):
        if new_list[i] == '_':
            if original_list[i] == letter.lower() or original_list[i] == letter.upper():
                new_list[i] = letter
    os.system('cls')
    for letter in new_list:
        print(letter,end="")
    print()
    print("\t\t\t Lives remaining:",lives)
    print("\t\t\t",end=" ")
    for letter in temp:
        print(letter,end=" ")
    print_man(lives)

while True:
    choice = input("Start game? (y,n): ")
    os.system('cls')
    if choice == ('n' or 'N'):
        print("Bye")
        break
    else:
        temp = []
        lives = 6
        main()



