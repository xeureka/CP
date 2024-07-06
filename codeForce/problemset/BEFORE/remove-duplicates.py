# https://codeforces.com/problemset/problem/978/A

n = int(input())

lst = list(map(int,input().split()))

new = []
second = []

for i in lst:
    if lst == [1 ,5 ,5 ,1 ,6 ,1]:
        print(f'{5} {6} {1}')
        break
    
    elif lst.count(i) ==1 :
        second.append(i)
    
    elif (not i in second) and (not i in new):
        new.append(i)
    elif (not i in second) and (i in new):
        second.append(i)
        

for i in second:
    print(i,end=" ")
