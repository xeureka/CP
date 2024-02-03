'''058




Make a maths quiz that asks five questions by randomly
generating two whole numbers to make the question
(e.g. [num1] + [num2]). Ask the user to enter the
answer. If they get it right add a point to their score. At
the end of the quiz, tell them how many they got correct
out of five.
'''

import random

print('WELCOME TO THE QUIZ')

num1 = random.randint(1,100)
num2 = random.randint(1,100)


score = 0
add = num1 + num2
add1 = int(input((f'1. {num1} + {num2} = ')))
if add1 == add:
    score +=1


