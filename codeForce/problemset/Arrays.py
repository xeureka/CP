# https://codeforces.com/problemset/problem/572/A

A,B = map(int,input().split())
k,m = map(int,input().split())

arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

coutK = 0
coutM = 0

for i in arr1:
    for j in arr2:
        if i > j:
            coutK +=1
            coutM += 1
            print('YES')
            break


