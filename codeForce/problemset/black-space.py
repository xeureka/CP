
# https://codeforces.com/contest/1829/problem/B

for i in range(int(input())):
    n = int(input())
    lst = list(map(int,input().split()))
    cout = 0
    new = []

    for j in lst:
        try:
            if (j ==0) and(lst[j + 1] ==0 ):
                cout +=1
            else:
                new.append(cout)
                cout = 0
        except:
            break

    if lst.count(0) ==1:
        print(1)
    else:
        print(max(new))
        