
# https://codeforces.com/problemset/problem/750/A


n,k = map(int,input().split())

hr = 4*60
cont = hr - k

prob = 0

time = 0

for i in range(1,n+1):
    time += i*5

    if time <= cont:
        prob +=1
    else:
        break
print(prob)

