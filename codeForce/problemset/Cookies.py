# https://codeforces.com/gym/537460/problem/A

n = int(input())

arr = list(map(int,input().split()))

count = 0

summ = sum(arr)

for i in arr:
    summ -= i

    if summ % 2 ==0:
        count += 1

    summ = sum(arr)


print(count)
    
