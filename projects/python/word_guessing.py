

import random

word = ['Red','Green','White','Blue','Purple']

x = random.choice(word)

try:
    user_in = input('ENter you guess here:  ')
except TypeError as e:
    print(e)
except ValueError as e:
    print(e)
except:
    print('We encounter some error here')

else:
    score = 0
    for i in range(5):
        if user_in == x:
            score +=1
            print('You get correctly')

    print(f'You score {score} points')