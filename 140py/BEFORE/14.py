#Write a Python Program to Check Prime Number.

num = int(input('Enter a number: '))

val = 0

for i in range(2,num):
    if num % i ==0:
        val +=1

if val > 0:
    print('not prime')
else:
    print('prime number')