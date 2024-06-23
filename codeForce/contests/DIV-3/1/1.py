# https://codeforces.com/contest/1986/problem/A



for i in range(int(input())):
    x,y,z = map(int,input().split())

    arr= []
    arr.append(x)
    arr.append(y)
    arr.append(z)

    print(max(arr) - min(arr))


