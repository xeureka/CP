#Write a Python program to swap two variables.

a = int(input('num 1: '))
b = int(input('num 2: '))

print(f'inital values: a={a}, b={b}')
a,b = b,a

print(f'final values: a={a}, b={b}')