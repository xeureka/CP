
# https://codeforces.com/contest/1760/problem/C

for i in range(int(input())):
    n = int(input())

    lst = list(map(int,input().split()))

    maX = max(lst)

    new1 = lst.copy()
    new1.remove(maX)
    maY = max(new1)

    ans = []

    for i in lst:
        if i == maX:
            ans.append(maX - maY)
        else:
            ans.append(i - maX)

    for i in ans:
        print(i,end = ' ')
    