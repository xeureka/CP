'''

Ask the user to
enter four of their
favourite foods
and store them in
a dictionary so
that they are
indexed with
numbers starting
from 1. Display
the dictionary in
full, showing the
index number
and the item. Ask
them which they
want to get rid of
and remove it
from the list. Sort
the remaining
data and display
the dictionary.


'''

foods = input().split()

foods = dict(foods)
print(foods)
