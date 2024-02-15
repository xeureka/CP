# Exercise 3: Turn every item of a list into its square


lst = list(map(int,input().split()))

result = list(map(lambda x:x**2,lst))

print(result)
