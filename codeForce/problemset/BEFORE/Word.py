# https://codeforces.com/problemset/problem/59/A



word = input()

upp = 0
loe = 0

for i in word:
    if i == i.upper():
        upp +=1
    else:
        loe +=1


if upp > loe:
    print(word.upper())
else:
    print(word.lower())
