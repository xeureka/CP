# https://codeforces.com/problemset/problem/1915/A
n = int(input())

for i in range(n):
    a,b,c = map(int,input().split())

    lst = [a,b,c]

    if lst.count(a) ==1:
        print(a)
    elif lst.count(b) ==1:
        print(b)
    else:print(c)