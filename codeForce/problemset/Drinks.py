# https://codeforces.com/problemset/problem/200/B

n = int(input())

arr = list(map(int,input().split()))

answer = sum(arr) / n

print(round(answer,12))