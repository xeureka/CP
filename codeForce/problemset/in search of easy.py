
# https://codeforces.com/problemset/problem/1030/A

n = int(input())

lst = list(map(int,input().split()))

if 1 in lst:
    print('HARD')
else:
    print('EASY')