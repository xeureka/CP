from collections import Counter

nums = [1,1,1,2,2,3]
k = 2

lst = []

nums = list(set(nums))

nums.sort(reverse = True)

print(nums[:k])

