'''

Add to program 069 to ask the
user to enter a number and
display the country in that
position.

'''



countries = ('ETHIOPIA','ERTERIA','RUSSIA','CUBA','UGANDA')

for i in countries:
    print(i)

user = int(input('Enter the number of the country:  '))

print(countries[user])