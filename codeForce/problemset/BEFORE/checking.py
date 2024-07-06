# https://codeforces.com/problemset/problem/1791/A

word = list('codeforces')

t = int(input())
for i in range(t):
    x = input()
    if x in word:
        print('YES')
    else:
        print('NO')
