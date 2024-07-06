# https://codeforces.com/problemset/problem/1692/A

n = int(input())
for i in range(n):
    arr = list(map(int,input().split()))
    tim = arr[0]
    cout = 0

    for i in arr:
        if i > tim:
            cout +=1
    print(cout)