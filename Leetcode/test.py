words = ["bella","label","roller"]

words = tuple(words)

first,*rest = words
ans = []

for i in first:
    for j in rest:
        if i in j:
            ans.append(i)

print(ans)