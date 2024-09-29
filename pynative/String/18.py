# Exercise 18: Replace each special symbol with # in the following string

str1 = '/*Jon is @developer & musician!!'

new = ''

for i in str1:
    if i.isalnum() or i == ' ':
        new += i
    else:
        new += '#'

print(new)