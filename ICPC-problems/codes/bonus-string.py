lst = []

for i in range(3):
    x = input()
    lst.append(x)

lst.sort()
lst.sort(key=len)


for i in lst:
    print(i)