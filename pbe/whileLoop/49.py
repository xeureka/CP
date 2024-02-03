'''
049

Create a variable called
compnum and set the value
to 50. Ask the user to enter a
number. While their guess
is not the same as the
compnum value, tell them if
their guess is too low or too
high and ask them to have
another guess. If they enter
the same value as
compnum, display the
message “Well done, you
took [count] attempts”.

'''

compnum = 50
count = 0


while compnum != guess:
    guess = int(input('ENter a number: '))
    if guess > compnum:
        print('Too high')
    else:
        print('Too low')

    
    count +=1

print(f'Well done you took, {count} attempts')