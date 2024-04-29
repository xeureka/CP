# https://codeforces.com/problemset/problem/467/A


n = int(input())


cout = 0
for i in range(n):
    
    p,q = map(int,input().split())

    if q - p >= 2:
        cout +=1

print(cout)
        

    