# https://cses.fi/problemset/task/1068

n = int(input())

ans = []

while n >= 1:
    if n % 2 ==0:
        n /= 2
        ans.append(n)
    else:
        n = 3*n + 1
        ans.append(n)

print(ans)