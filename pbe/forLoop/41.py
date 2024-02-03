'''
041

Ask the user to enter their
name and a number. If the
number is less than 10, then
display their name that
number of times; otherwise
display the message “Too
high” three times.

'''

name = input('Enter your name: ')
num = int(input('ENter any number: '))


if 0 < num <= 10:
    for i in range(num):
        print(name)
else:
    print('The number is too high')