# https://codeforces.com/problemset/problem/1866/A


n = int(input())
arr = list(map(int,input().split()))

pos = [x for x in arr if x >=0]
neg = [x for x in arr if x < 0]

neg = [-x for x in neg]

ans = neg+ pos

print(min(ans))