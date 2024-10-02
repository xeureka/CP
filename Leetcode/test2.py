from collections import Counter

paragraph = "a. a a is eureka teklemariam haile"
banned = []

print(banned == [])

new = ''

for i in paragraph:
    if i.isalpha() or i == ' ':
        new += i.lower()

new.strip()

lst = new.split()

new = dict(Counter(lst))


items = [i for i in new.items()]
values = [i for i in new.values()]

fr = max(values)

for i in items:
    for j in i:
        if j == fr:
            print(i[0])