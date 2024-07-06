# https://codeforces.com/problemset/problem/271/A
from collections import Counter

year  = int(input())

def dis_year(year):
    new = Counter(str(year))

    value = True

    for item in new:
        if new[item] ==1:
            value = True
        else:
            break

        return value
        


for i in range(year+1,9000):
    if dis_year(year):
        print(i)
        break