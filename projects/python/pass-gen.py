
# This is random password generator for users

# our password container word letters numbers and symplos in combination and it must have to be a length of 8 characters

import random

nums = list(range(0,10))
capitalLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

smallLetters = []

for i in capitalLetters:
    smallLetters.append(i.lower())



print(smallLetters)