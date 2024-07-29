# https://open.kattis.com/problems/cold


cout = 0

n = int(input())

lst = list(map(int,input().split()))

for i in lst:
    if i < 0:
        cout += 1

print(cout)