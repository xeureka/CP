# https://codeforces.com/problemset/problem/469/A


n = int(input())

p = list(map(int,input().split()))
q = list(map(int,input().split()))

del p[0]
del q[0]

total = p + q

total = set(total)
total = list(total)
total.sort()

if total[-1] ==n:
    print('I become the guy')
else:
    print('Oh, my keyboard!')