# https://codeforces.com/problemset/problem/339/A



exp = input().split('+')

exp.sort()

new = ''

for i in exp:
    new += '+' + i

new1 = new[1:]

print(new1)