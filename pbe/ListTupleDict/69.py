'''
Create a tuple containing the names of five countries and display the whole tuple. Ask
the user to enter one of the countries that have been shown to them and then display
the index number (i.e. position in the list) of that item in the tuple.

'''


countries = ('ETHIOPIA','ERTERIA','RUSSIA','CUBA','UGANDA')

for i in countries:
    print(i)

user = input('Enter the name of the country from the above lists:  ').upper()

if user not in countries:
    print('Pleas select from the list')
else:
    print(countries.index(user))

