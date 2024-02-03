'''
011
Task the user to enter a number over 100 and then enter a number under
10 and tell them how many times the smaller number goes into the larger
number in a user-friendly format.

'''

largeNum = int(input('Enter number over 100: '))
smallerNum = int(input('Enter number under 10: '))

ratio = largeNum / smallerNum

print(f'{largeNum} goes over {smallerNum} in {ratio} times.')

