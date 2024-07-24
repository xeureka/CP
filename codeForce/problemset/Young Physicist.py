# https://codeforces.com/gym/512827/problem/C



n = int(input())

a =[]
b = []
c = []

for i in range(n):
    lst = list(map(int,input().split()))
    a.append(lst[0])
    b.append(lst[1])
    c.append(lst[2])

if sum(a) == 0 and sum(b) ==0 and sum(c) == 0:
    print('YES')
else:
    print('NO')
    