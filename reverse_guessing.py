import random,os
choice = None
def main(lower,upper,lives):
    guess=random.randint(lower,upper)
    response = None
    while True:
        response = input(f"Is the number {guess}? ")
        if response == 'YES':
            print("\nAI WON!\nMoral:Never underestimate an AI!\n(and please save the embarresment.......)\n")
            break
        elif response=='H':
            lower = guess+1
            guess = random.randint(lower,upper)
        elif response=='L':
            upper = guess-1
            guess = random.randint(lower,upper)
        lives -= 1
        if lives==0:
            print('\n[AI LOST!] :(:(:(')
            print("\nMoral:The notion that computers are smarter than humans appears to be total bull.\nYou won! ;)\n")
            break
while choice !='N':
    print()
    print("###WELCOME TO AI VS HUMAN GUESSING#######")
    print()
    input("Think of a number between 1 and 50\nThe computer will try guessing,\nyou need to say if its higher(H),lower(L) or equal(YES) to it.\nHit enter to continue....\n")
    lower = 1
    upper = 50
    lives = 5
    try:
        main(lower,upper,lives)
    except:
        print("\nYou are lying! Puny Human!")
    choice = input("Again? (Y,N): ")
    os.system('cls')
