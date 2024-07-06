# https://codeforces.com/problemset/problem/707/A

n,m = map(int,input().split())

lst = []

for i in range(n):
    pixel = input().split()
    lst.append(pixel)


BwG = ['B','W','G']

value = []

for item in lst:
    for i in item:
        if not i in BwG:
            value.append(0)
            break
        else:
            value.append(1)

if value.count(1) == len(value):
    print('#Black&White')
else:
    print('#Color')