#Write a Python Program to Check if a Number is Positive, Negative or Zero.


num = float(input('Enter a number: '))

if num >0:
    print(f'{num} is postive')
elif num <0:
    print(f'{num} is negative')
else:
    print(f'{num} is zero')