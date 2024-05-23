# https://cses.fi/problemset/task/1083

n = int(input())

lst = list(map(int,input().split()))

lst.sort()

for i in range(n):
    for i in lst:
        if lst[i] 