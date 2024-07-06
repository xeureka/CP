# https://codeforces.com/problemset/problem/1472/B
from collections import Counter

for i in range(int(input())):
    n = int(input())
    lst = list(map(int,input().split()))

    count = Counter(lst)

    new = [i for i in count.values()]
    if len(count) % 2 != 0:
        print('NO')
        
    elif (count[1] % 2 ==0) and (count[2] % 2 ==0):
        print('YES')

    elif len(lst) % 2 ==0:
        if lst.count(1) ==0 and lst.count(2) % 2 ==0:
            print('YES')
        elif lst.count(1) % 2 ==0 and lst.count(2) ==0:
            print('YES')
        else:
            print('NO')
           
    else:
        print('NO')
         

    