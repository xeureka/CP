arr = [1,3,6,2,6]

rank = {}

for i in sorted(arr):
    if not i in rank:
        rank[i] = len(rank) + i

print(rank[i] for i in arr)