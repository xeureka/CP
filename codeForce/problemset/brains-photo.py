# https://codeforces.com/problemset/problem/707/A

n,m = map(int,input().split())

lst = []

for i in range(n):
    pixel = input().split()
    lst.append(pixel)


bw = ['B','W']

for i in lst:
    if i not in bw:
        print('#Color')
        break
    else:
        print('#Black&White')