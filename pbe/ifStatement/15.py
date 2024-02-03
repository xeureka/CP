'''
015
Ask the user to enter their favourite colour. If they enter “red”, “RED” or
“Red” display the message “I like red too”, otherwise display the message
“I don’t like [colour], I prefer red”.
'''
color = input('enter your favorite color: ').lower()

if color == 'red':
    print('I like red too.')
else:
    print(f'I dont like {color} , I prefer red')
    