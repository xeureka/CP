# https://codeforces.com/gym/512827/problem/C

n = int(input())

arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
arr3 = list(map(int,input().split()))

new = []

cob = tuple(zip(arr1,arr2,arr3))
x,y,z = cob
    
x1 = sum(x)
y1 = sum(y)
z1 = sum(z)

new = [x1,y1,z1]
if new == [0,0,0]:
    print('YES')
else:
    print('NO')