# https://codeforces.com/gym/540499/problem/E

n = int(input())
lst = list(map(int,input().split()))

def tPrime(num):
    cout = 0

    for i in range(1,num+1):
        if num % i ==0:
            cout += 1

            if cout >3:
                return False

    if cout != 3:
        return False
    else:
        return True


for i in lst:
    if tPrime(i):
        print('YES')
    else:
        print('NO')


