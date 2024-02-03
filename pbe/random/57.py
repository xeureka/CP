'''
057

Update
program 056
so that it
tells the
user if they
are too high
or too low
before they
pick again.

'''
import random

while True:
    ask = int(input('Enter a number between 1 and 10: '))

    num = random.randint(1,10)


    if ask == num:
        print('You get the answer write')
        break
    else:
        if ask > num:
            print('You are to high')
        else:
            print('You are too high')
        continue


