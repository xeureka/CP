'''
Create a list of two sports. Ask the
user what their favourite sport is and
add this to the end of the list. Sort the
list and display it.

'''

sport = ['foot ball','basket ball']

user_sport = input('ENter your favorite sport: ')

sport.append(user_sport)

sport.sort()

for i in sport:
    print(i)