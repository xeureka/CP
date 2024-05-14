# https://codeforces.com/contest/1669/problem/B

for i in range(int(input())):
    n = int(input())
    lst = list(map(int,input().split()))

    cout = 0
    new = []

    for i in lst:
        if lst.count(i) >=3:
            cout +=1
            new.append(i)
            break

    if cout >=1:
        print(new[0])
    else:
        print(-1)
            

        