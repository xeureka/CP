'''
039

Ask the user to enter a number between 1
and 12 and then display the times table for
that number.

'''


num = int(input('ENter a number between 1 and 12: '))

if 1<= num <= 12:
    for i in range(1,13):
        print('%d x %d = %d' %(num,i,num*i))

    else:
        print('please enter a number in a given range.')