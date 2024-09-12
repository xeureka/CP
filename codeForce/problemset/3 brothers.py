# https://codeforces.com/problemset/problem/2010/B


lst = list(map(int,input().split()))

ans = [1,2,3]


for i in ans:
    if not i in lst:
        print(i)



