# https://codeforces.com/problemset/problem/469/A


n = int(input())


x = list(map(int,input().split()))
y = list(map(int,input().split()))

check = list(range(1,n+1))

newX = x[1:]
newY = y[1:]

arr = newX + newY
arr = set(arr)

arr = list(arr)
arr.sort()

if arr == check:
    print('I become the guy.')
else:
    print('Oh, my keyboard!')