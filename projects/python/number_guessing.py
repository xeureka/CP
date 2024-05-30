

import random

comp_guess = random.randrange(1,10)

try:
    user_guess = int(input('Enter you guess from 1 to 10:   '))
except TypeError as e:
    print(e)
except ValueError as e:
    print(e)

else:
    score = 0

    for i in range(5):
        if user_guess == comp_guess:
            score +=1
            print(f'You got the answer correctly')
    
    print(f'Horray your score is {score}')


