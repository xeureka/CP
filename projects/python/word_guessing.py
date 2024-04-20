
import random

start = ['Ethiopia','Kenya','Sudan','Erteria','Djibuti','Uganda','Rwanda']

answer = random.choice(start)

count = 0
attempts = 5
value = False

print("guess an east african country")
while attempts < 0:
    user_input = input('Enter your guess:  ').title()

    count +=1
    if user_input == answer:
        print(f'You got the answer is {count} attempts')
        value = True
        break
    else:
        attempts -=1
        print(f'Try again you have {attempts} attempts left ')

if value == False:
    print('You lose, please try again')
    