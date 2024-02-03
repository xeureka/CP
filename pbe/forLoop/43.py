'''
043

Ask which direction the user wants to count (up or down). If they select up, then ask
them for the top number and then count from 1 to that number. If they select down, ask
them to enter a number below 20 and then count down from 20 to that number. If they
entered something other than up or down, display the message “I don’t understand”.

'''

ask = input('up or down: ').lower()

if ask == 'up':
    upper = int(input('Enter un upper number: '))

    for i in range(1,upper+1):
        print(i)
elif ask == 'down':
    lower = int(input('Enter a lower number: '))

    for i in range(lower,0,-1):
        print(i)
else:
    print('I cant understand your input')
