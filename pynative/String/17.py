# Exercise 17: Find words with both alphabets and numbers

str1 = "Emma25 is Data scientist50 and AI Expert"

new = str1.split()

ans = []

for i in new:
    if any(char.isalpha() for char in i) and any(char.isdigit() for char in i):
        ans.append(i)

for i in ans:
    print(i)