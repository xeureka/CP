list1 = list(map(int,input().split()))
list2 = list(map(int,input().split()))

new = []

for i in list1:
    if i % 2 ==0:
        new.append(i)

for i in list2:
    if i % 2 != 2:
        new.append(i)

new.sort()
print(new)
