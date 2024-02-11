# This is a program that selects random number form a given range just like the betting number games


import random

user = list(map(int,input('Enter five numbers form the range of 1 to 80: ').split()))


lst = []
for i in range(10):
    computer = random.randrange(1,80)
    lst.append(computer)

    print(f'number: {computer}')

lst.sort()
user.sort()

count = 0
if user ==lst:
    print(f'Kudo you win you got all numbers right')
else:
    for i in user:
        if i in lst:
            count +=1
    print(f'You got {count} guess right')