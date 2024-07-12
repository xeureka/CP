# https://codeforces.com/problemset/problem/1328/A


for i in range(int(input())):
    a,b = map(int,input().split())
    
    v = a/b

    if v - int(v) ==0:
        print(0)
    else:
        n = b*(int(v) +1)
        print(n -b)

    

    


    