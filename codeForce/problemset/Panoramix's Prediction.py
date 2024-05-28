# https://codeforces.com/problemset/problem/80/A


a,b = map(int,input().split())


def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


if (prime(a) == True) and (prime(b) == True):
    pr = []

    for i in range(a,b+1):
        if prime(i):
            pr.append(i)

    if pr.index(b) == pr.index(a) + 1:
        print('YES')
    else:
        print('NO')

else:
    print('NO')

