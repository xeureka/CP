'''
Write a Python program to solve quadratic equation.
    The standard form of a quadratic equation is:
        ax2 + bx + c = 0
    where
        a, b and c are real numbers and
            a≠0
The solutions of this quadratic equation is given by:


'''


import math

a= float(input('Enter the coeficent of x2: '))
b = float(input('Enter the coeficent of x: '))
c = float(input('Enter the coeficent of 0*x: '))

dis = (b**2 -4*a*c)


if dis >0:
    x1 = (-b + math.sqrt(dis)) / (2*a)

    x2 = (-b - math.sqrt(dis)) / (2*a)


    print(f'The two solutions of the equation is {x1} and {x2}')

if dis <0:
    print('The function has no solution')
    
else:
    print('The function has one solution')