# https://codeforces.com/problemset/problem/1722/B

n = int(input())


for i in range(n):
    t = int(input())

    arr1 = input()
    arr2 = input()

    comb = list(zip(arr1,arr2))

    cout = 0

    for i in comb:
        if 'R' in i:
            cout +=1

    if cout >=1:
        print('NO')
    else:
        print('YES')