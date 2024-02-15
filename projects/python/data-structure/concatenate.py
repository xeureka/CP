# Exercise 2: Concatenate two lists index-wise


first = ['M','na','i','eu']
second = ['y','me','s','reka']


# final = ["My",'name','is','eureka']

result = [ i + j for i ,j in zip(first,second) ]

print(result)