# https://codeforces.com/problemset/problem/977/A

num,step = map(int,input().split())

for i in range(step):
    if num % 10 ==0:
        num /= 10
    else:
        num -=1

print(int(num))