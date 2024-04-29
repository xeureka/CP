# https://codeforces.com/problemset/problem/1760/A

t = int(input())

for i in range(t):
    new = []
    lst = list(map(int,input().split()))

    x = max(lst)
    new.append(x)
    y = min(lst)
    new.append(y)

    for j in lst:
        if not j in new:
            print(j)
    
    



