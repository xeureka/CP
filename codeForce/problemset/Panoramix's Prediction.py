# https://codeforces.com/problemset/problem/80/A



a,b = map(int,input().split())


def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

pri= []

for i in range(2,51):
    if prime(i):
        pri.append(i)


index = pri.index(a)

if pri[index + 1] == b:
    print('YES')
else:
    print('NO')