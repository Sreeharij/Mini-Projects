import time,os
head = '''
        /-----\\
        | -  - |
        |  |   |
        |      |
        \\------/  '''
trunk= head+'''
           |
           |
           |
           |
           |
           |    '''

left_arm = head + '''
           |
           |
          /|
         / |
           |
           |  '''

right_arm = head + '''
           |
           |
          /|\\
         / | \\
           |
           |   '''

left_leg = right_arm + '''
          /
         /      '''
right_leg = right_arm + '''
          / \\
         /   \\
        GAME OVER!!! '''

body = [head,trunk,left_arm,right_arm,left_leg,right_leg]
def print_man():
    #Just a function to demonstrate progressive display!
    for item in body:
        os.system('cls')
        print(item)
        time.sleep(1)

