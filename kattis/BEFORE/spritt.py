st,sa = map(int,input().split())

lst = []
for i in range(st):
    num = int(input())
    lst.append(num)


if sa >= sum(lst):
    print('Jebb')
else:
    print('Neibb')
