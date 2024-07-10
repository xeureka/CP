lst = [5, 10, 15, 20, 25, 50, 20]


# replace 20 with 200

for i in range(len(lst)):
    if lst[i] == 20:
        lst[i] = 200
        break

print(lst)