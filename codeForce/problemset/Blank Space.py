# https://codeforces.com/problemset/problem/1829/B


for i in range(int(input())):

    num = int(input())
    n = list(map(int,input().split()))

    cnt,ans = 0,0

    for i in n:
        if i ==0:
            cnt +=1
        else:
            ans = max(cnt,ans)
            cnt = 0

    answer = max(cnt,ans)
    print(answer)


