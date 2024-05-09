# https://codeforces.com/problemset/problem/59/A

s = input()

cout = 0
cout1 = 0

for i in s:
    if i.islower():
        cout +=1
    else:
        cout1 +=1

if cout >=cout1:
    print(s.lower())
else:
    print(s.upper())

