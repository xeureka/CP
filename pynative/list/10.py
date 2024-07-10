lst = [5, 20, 15, 20, 25, 50, 20]

# write a program to remove all occurances of item 20

for i in lst:
    if i == 20:
        lst.remove(i)

print(lst)