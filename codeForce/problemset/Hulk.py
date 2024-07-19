# https://codeforces.com/problemset/problem/705/A


n = int(input())

hate = 'I hate that '
love = 'I love that '


ans = ''

for i in range(1,n+1):
    if i % 2 ==0:
        ans += love
    else:
        ans += hate

new = ''

new = ans[:-5] + 'it'
print(new)