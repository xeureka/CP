# https://codeforces.com/problemset/problem/1742/A

t = int(input())

for i in range(t):
    a,b,c = map(int,input().split())

    if (a+b==c) or (a+c==b) or (b+c ==a):
        print('YES')
    else:
        print('NO')
