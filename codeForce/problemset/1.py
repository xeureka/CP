# https://codeforces.com/gym/511717/problem/A

n = int(input())
count = 0

for i in range(1,n+1):
    p,v,t = map(int,input().split())

    if p + v +t >= 2:
        count +=1
print(count)

