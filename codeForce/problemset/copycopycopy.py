# https://codeforces.com/problemset/problem/630/A

for i in range(int(input())):
    n = int(input())

    lst = list(map(int,input().split()))

    print(len(set(lst)))