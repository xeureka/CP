# Exercise 5: Iterate both lists simultaneously


lst1 = list(map(int,input().split()))
lst2 = list((map(int,input().split())))


result = dict(zip(lst1,lst2))

for key,value in result.items():
    print(key,value)

