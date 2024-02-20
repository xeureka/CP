# Exercise 6: Remove empty strings from the list of strings


# strings = list(map(str,input().split()))

strings = ["Mike", "", "Emma", "Kelly", "", "Brad"]


fil = [i for i in strings if len(i)>=1]
print(fil)