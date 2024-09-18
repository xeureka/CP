


n = int(input())

lst = list(map(int,input().split()))

lst.sort(reverse=True)



count = 0
summ = sum(lst)
twin = 0


for i in lst:
    twin += i
    if twin < (summ-i):
        count += 1
    else:
        break
print(n-count)
    
