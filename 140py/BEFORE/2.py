#Write a Python program to do arithmetical operations addition and division.

num1 = float(input('Enter the first number: '))
num2 = float(input('ENter the second number: '))

add = num1 + num2

if num2 == 0:
    print('We canot divide number by 0 ')
else:
    div = num1 / num2

print(f'{num1} + {num2} = {add}\n{num1} / {num2} = {div}')