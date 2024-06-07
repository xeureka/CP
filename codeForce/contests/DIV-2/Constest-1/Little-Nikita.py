
# https://codeforces.com/contest/1977/problem/A


n = int(input())

for i in range(n):
    n,m = map(int,input().split())


    if n ==m:
        print('YES')
    elif m >n:
        print('NO')

    elif n >m:
        rest = n - m
        rest = n - m
        
        if rest % 2 == 0:
            print('YES')
        else:
            print('NO')

