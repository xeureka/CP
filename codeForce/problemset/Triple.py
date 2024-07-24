# https://codeforces.com/problemset/problem/1669/B


from collections import Counter

for i in range(int(input())):
    num = int(input())
    arr = list(map(int,input().split()))

    count = Counter(arr)
    lst = []


    if num < 3:
        print(-1)
    else:
        for i,j in count.items():
            if j >= 3:
                print(i)
                break
        else:
            print(-1)



    # ans = [(i,j) for i,j in count.items()]
    # lst = []

    # if num < 3:
    #     print(-1)
    # else:
    #     for i in ans:
    #         if i[1] >=3:
    #             print(i[0])
                
    #             break
    #     else:
    #         print(-1)

        
