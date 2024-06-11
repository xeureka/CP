# https://codeforces.com/contest/1985/problem/A

t = int(input())

for i in range(t):
    a,b = map(str,input().split())

    char_a = a[0]
    char_b = b[0]

    new_a = char_b + a[1:]
    new_b = char_a + b[1:]

    print(new_a,new_b)