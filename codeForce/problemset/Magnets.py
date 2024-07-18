# https://codeforces.com/problemset/problem/344/A


n = int(input())

lst = []

for i in range(n):
    pole = input()
    lst.append(pole)

group = 0
cout = 0

for i in range(n):
    try:

        new = lst[i]
        next = lst[i + 1]
        
        if new != next:
            group+=1
            
    except:
        break

    
print(group + 1)

