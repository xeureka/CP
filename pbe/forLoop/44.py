'''
044

Ask how many people the user wants to invite to a party. If they enter a number below
10, ask for the names and after each name display “[name] has been invited”. If they
enter a number which is 10 or higher, display the message “Too many people”.

'''

num = int(input('how many people did u want to invite to the party: '))

if 0< num <= 10:
    for i in range(num):
        name = input('Enter the name of each persn: ')
        print(f'{name} has been invited')
else:
    print('You entered to many peoples')