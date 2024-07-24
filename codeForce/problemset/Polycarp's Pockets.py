# https://codeforces.com/problemset/problem/1003/A

from collections import Counter

n = int(input())

lst = list(map(int,input().split()))

count = Counter(lst)

answer = [[i,j] for i,j in count.items()]

max = 0

for item in answer:
    if item[1] > max:
        max = item[1]
        
print(max)
