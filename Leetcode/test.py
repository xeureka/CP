arr = [2,2,2,3,3]



lucky = []

for i in arr:
    if i == arr.count(i):
        lucky.append(i)


if len(lucky) >= 1:
    print(max(lucky))
else:
    print(-1)

