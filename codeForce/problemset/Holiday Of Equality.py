# https://codeforces.com/problemset/problem/758/A

n = int(input())

lst = list(map(int,input().split()))

max = max(lst)

cout = 0

for i in lst:
    if i != max:
        cout += max - i

print(cout)