
import random


answer = random.randint(1,50)


print('Welcome to the number guessing game')
print('- You have 7 tries enjoy the game')


user = int(input('Enter 1 to start the game:  '))

if user ==1:
    count =0
    value = False
    while count <=7:
        user_input = int(input('Guess a number between 1 to 50: '))
        count +=1
        if user_input == answer:
            print(f'Yess, you got the answer in {count} attempts')
            value = True
            break
        else:
            if answer > user_input:
                print('Too low try larger number')
            else:
                print('Too low try larger number')
    if value == False:
        print('You lose the game please return next time.')