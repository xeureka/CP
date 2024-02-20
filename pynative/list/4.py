# Exercise 4: Concatenate two lists in the following order


list1 = list(map(str,input().split()))

list2 = list(map(str,input().split()))

result = [i+' '+j for i,j in zip(list1,list2)]
print(result)