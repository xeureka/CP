# https://cses.fi/problemset/task/1083

def missNum(num,n):
    
    for i in range(1,n+1):
        if i not in num:
            return i
        
n = int(input())
lst = set(map(int,input().split()))

print(missNum(lst,n))