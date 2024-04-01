# https://codeforces.com/problemset/problem/41/A


t = input()
s= input()


rev_s = s[::-1]

if t==rev_s:
    print('YES')
else:
    print("NO")