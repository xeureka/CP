# Exercise 6: Remove empty strings from the list of strings

# words = list(map(str,input().split()))
words = ["Mike", "", "Emma", "Kelly", "", "Brad"]

# method 1
for i in words:
    if len(i) ==0:
        words.remove(i)

print(words)

# method 2 using list comphrension

new = [i for i in words if len(i) !=0]

print(new)