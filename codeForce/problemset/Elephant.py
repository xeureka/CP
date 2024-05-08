# https://codeforces.com/problemset/problem/617/A


def min_step(x):
    return (x//5) + (1 if x %5 != 0 else 0)

n = int(input())

print(min_step(n))