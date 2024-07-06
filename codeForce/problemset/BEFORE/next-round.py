# https://codeforces.com/problemset/problem/158/A

n, t = map(int, input().split())
lst = list(map(int, input().split()))

tot = 0
for i in lst:
    if i >= lst[t-1] and i != 0:
        tot += 1

print(tot)