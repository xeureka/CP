# https://codeforces.com/contest/1676/problem/B

for i in range(int(input())):
    n =int(input())
    lst = list(map(int,input().split()))

    minn = min(lst)

    ans = sum([i-minn for i in lst ])
    print(ans)