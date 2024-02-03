'''

056

Randomly pick a whole number between 1
and 10. Ask the user to enter a number and
keep entering numbers until they enter the
number that was randomly picked.

'''
import random

while True:
    ask = int(input('Enter a number between 1 and 10: '))

    num = random.randint(1,10)


    if ask == num:
        print('You get the answer write')
        break
    else:
        continue

