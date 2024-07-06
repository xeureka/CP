

t = int(input())
lst1 = []
lst2 = []
for i in range(t):
    name,num = map(str,input().split())
    num = int(num)
    
    lst1.append(name)
    lst2.append(num)

    my = dict(zip(lst2,lst1))

x = my.keys()
x = list(x)

z = max(x)

print(my[z])

