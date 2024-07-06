# https://codeforces.com/problemset/problem/546/A


k,n,w = map(int,input().split())


total = 0

for i in range(1,w+1):
    total += i * k

borrow = total - n

if borrow <=0:
    print(0)
else:
    print(borrow)


