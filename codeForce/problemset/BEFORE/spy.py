# https://codeforces.com/gym/512827/problem/A

t = int(input())

for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))

    new = set(arr)
    new = tuple(new)
    x,y = new
    
    if arr.count(x) > 1:
        z = arr.index(y)
    else:
        z = arr.index(x)

    print(z + 1)