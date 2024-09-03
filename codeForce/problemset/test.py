for i in range(int(input())):
    a,b = map(int,input().split())

    ans = []

    for c in range(a+1,b):
        val = (c - a) + (c - b)
        ans.append((val,c))

    ans.sort()

    print(ans)
        


