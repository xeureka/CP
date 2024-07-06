# https://codeforces.com/problemset/problem/80/A

n,m = int(input())

def prime(num):
    lst = []
    for i in range(2,num):
        if num % i ==0:
            lst.append(i)
            break

    if len(lst) ==0:
        return True
    else:
        return False
    
for i in range(n,m+1):
    ans = []

    for j in range(1,i):
        if prime(i):
            ans.append(j)
            break

    if ans[0] == m:
        print('YES')
    else:
        print('NO')