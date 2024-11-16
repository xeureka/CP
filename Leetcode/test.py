from collections import Counter

nums = [2,2,1]

number = Counter(nums)

for i,j in number.items():
    if j == 1:
        print(i)