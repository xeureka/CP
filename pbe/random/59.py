'''

Display five colours and ask the user to pick one. If they
pick the same as the program has chosen, say “Well
done”, otherwise display a witty answer which involves
the correct colour, e.g. “I bet you are GREEN with envy”
or “You are probably feeling BLUE right now”. Ask
them to guess again; if they have still not got it right,
keep giving them the same clue and ask the user to
enter a colour until they guess it correctly.
'''



import random 

print('SELECT FROM THE FOLLOWING COLORS\n1.Green\n2.Blue\n3.Red\n4.white\n5.Grey')

color = random.choice(['green','blue','white','red','grey'])


color2 = input('SELECT YOUR COHOICE OF COLOR FROM THE ABOVE LIST: ')

if color == color2:
    print(f'You got the answer write keep guessing bro.')

else:
    print(f'What that the hell i was thing of {color} but you entered {color2}')