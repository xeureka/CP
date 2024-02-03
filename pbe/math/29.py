'''
029

Ask the user to enter an integer that is over 500. Work
out the square root of that number and display it to two
decimal places.

'''
from math import*
num = int(input('Enter an integer above 500: '))


squareRoot = sqrt(num)

print(round(squareRoot,2))