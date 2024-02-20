# Exercise 2: Concatenate two lists index-wise

list1 = list(map(str,input().split()))
list2 = list(map(str,input().split()))


result = [i + j for i,j in zip(list1,list2)]
print(result)