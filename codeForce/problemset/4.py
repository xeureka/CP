
# https://codeforces.com/gym/511717/problem/D

n = int(input())
l = int(input())


for i in range(n):
    name = input()

    lst = ['T','i','m','u','r']

    new = [j for j in name if j in lst]

    if len(new) == l:
        print('YES')
    else:
        print('NO')
