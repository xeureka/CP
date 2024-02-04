#Write a Python Program to Print the Fibonacci sequence.

num = int(input('ENter a number: '))

def fib(num):
    if num < 0:
        return 'Pleae enter a postive number.'
    else:
        return (num * fib(num-1))


print(fib(num))
