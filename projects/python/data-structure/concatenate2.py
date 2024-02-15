# Exercise 4: Concatenate two lists in the following order

lst1 = list(map(str,input().split()))

lst2 = list(map(str,input().split()))

result = [x +' '+ y for x in lst1 for y in lst2]

print(result)


#  this work correctly if and only if the lists have two items 