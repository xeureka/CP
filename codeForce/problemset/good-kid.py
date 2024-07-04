# https://codeforces.com/contest/1873/problem/B

for i in range(int(input())):
    n = int(input())
    lst = list(map(int,input().split()))
    lst.sort()
    
    mini = lst[0] + 1
    
    new = lst[1:]
    pro = 1

    for i in new:
        pro *=i
    
    print( pro * mini)