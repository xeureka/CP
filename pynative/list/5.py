# Exercise 5: Iterate both lists simultaneously

list1 = list(map(int,input().split()))

list2 = list(map(int,input().split()))

dic = dict(zip(list1,list2))

for key,value in dic.items():
    print(f'{key}  {value}')