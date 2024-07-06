#Write a Python Program to Check if a Number is Odd or Even.

num = int(input('ENter a number: '))


if num ==0:
    print('The number is zero')
elif num % 2 ==0:
    print(f'{num} is even')
else:
    print(f'{num} is odd')