
from collections import Counter

for i in range(int(input())):
    n = int(input())

    lst = list(map(str,input().split()))
    

    new = Counter(lst)
    cout = 0

    for item in new:
        if new[item] > 1:
            cout +=1
            break

    if cout > 0:
        print('NO')
    else:
        print('YES')

    