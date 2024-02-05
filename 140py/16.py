#Write a Python Program to Find the Factorial of a Number.


num = int(nput('Enter a number: '))

fact = 1

if num <0:
    print(f'The factorial of negative number is not exist')
else:
    for i in range(1,num+1):
        fact *=i

print(f'The factorial of the number is {fact}')