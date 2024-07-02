# https://codeforces.com/problemset/problem/1535/A

for i in range(int(input())):
    arr = list(map(int,input().split()))

    lst1 = arr[:2]
    ls2 = arr[2:]

    new = []
    new.append(max(lst1))
    new.append(max(ls2))

    val = min(new)

    fair = 0

    for i in arr:
        if i > val:
            fair +=1
    
    if fair > 1:
        print('NO')
    else:
        print('YES')