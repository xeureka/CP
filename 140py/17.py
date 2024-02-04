#Write a Python Program to Display the multiplication Table.

num = int(input('ENter a number: '))

for i in range(1,num+1):
    print(f'{num} x {i} = {num*i}')