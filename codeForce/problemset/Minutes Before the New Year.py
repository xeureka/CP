# https://codeforces.com/problemset/problem/1283/A


for i in range(int(input())):
    lst = list(map(int,input().split()))

    ans = ((24 - lst[0])*60) + (60 - lst[1])
    print(ans - 60)