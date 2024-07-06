# https://codeforces.com/problemset/problem/1328/A

for i in range(int(input())):
    x,y = map(int,input().split())

    if y > x:
        print(y - x)

    else:
        for i in range(x,10000):
            if i % y ==0:
                print(i - x)
                break