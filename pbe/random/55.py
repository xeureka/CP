'''
055


Randomly choose a number between 1 and 5. Ask the user to pick a
number. If they guess correctly, display the message “Well done”,
otherwise tell them if they are too high or too low and ask them to pick a
second number. If they guess correctly on their second guess, display
“Correct”, otherwise display “You lose”.

'''


import random

num = random.randint(1,5)


for i in range(2):
    ask = int(input('Enter yur guess: '))


    if ask == num:
        print('You won')
        break
    else:
       

        print('You lose')