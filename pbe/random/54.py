'''

054


Randomly choose either heads or tails (“h” or “t”). Ask
the user to make their choice. If their choice is the same
as the randomly selected value, display the message
“You win”, otherwise display “Bad luck”. At the end, tell
the user if the computer selected heads or tails.

'''

import random

coin = random.choice(['h','t'])

while True:
    ask = input('head or tail ').lower()

    if coin == ask:
        print(f'You win')
        break
    else:
        continue