'''
038

Change program
037 to also ask for a
number. Display
their name (one
letter at a time on
each line) and
repeat this for the
number of times
they entered.

'''

name = input('name: ')
num = int(input('Enter a number: '))

for i in range(1,num+1):
    for j in name:
        print(j)