# https://codeforces.com/problemset/problem/1335/A

t = int(input())

for i in range(t):
    n = int(input())

    count = 0
    for a in range(1,n):
        for b in range(1,n):
            if a>b and a+b == n:
                count +=1

    print(count)


