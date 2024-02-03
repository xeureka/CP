'''
048

Ask for the name of somebody the user wants to invite
to a party. After this, display the message “[name] has
now been invited” and add 1 to the count. Then ask if
they want to invite somebody else. Keep repeating this
until they no longer want to invite anyone else to the
party and then display how many people they have
coming to the party.

'''

count = 0

while True:
    name = input('ENter the name of the person: ')
    print(f'{name} has now been invited to the party')

    ask = input('did u wanna to add more people: ').lower()

    if ask == 'yes':
        continue
    else:
        break
print(f'{count} number of people are now invited to the party')


