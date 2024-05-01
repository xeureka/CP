# https://codeforces.com/problemset/problem/1952/H

t = int(input())

for i in range(t):
    word = input()
    rev= word[::-1]
    if  rev== word:
        print("YES")
    else:
        print("NO")