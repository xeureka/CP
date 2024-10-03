# xercise 9: Remove items from set1 that are not common to both set1 and set2

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set3 = set()

for i in set1:
    if i in set2:
        set3.add(i)
print(set3)


print(set1.intersection_update(set2))