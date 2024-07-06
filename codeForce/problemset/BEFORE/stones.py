# https://codeforces.com/problemset/problem/266/A

n = int(input())
lst = list(map(str,input().split()))

cout = 0
val =0

for i in range(0,len(lst)):
    if i == len(lst) -1:
        break

    else:
        if lst[i] == lst[i+1]:
            val+=1
            cout += 1
            

print(cout)
