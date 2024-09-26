import string

str1 = 'PyNaTive'

lower = list(string.ascii_lowercase)
upper = list(string.ascii_uppercase)

first = ''
second = ''

for i in str1:
    if i in lower:
        first += i
    else:
        second += i

print(first + second)