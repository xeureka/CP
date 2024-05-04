# https://codeforces.com/gym/512827/problem/C

n = int(input())

new = []
for i in range(n):
    lst = list(map(int,input().split()))

    new.extend(lst)


if sum(new) == 0:
    print('YES')
else:
    print('NO')