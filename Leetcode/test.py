from collections import Counter
from math import ceil


nums = [1]


b = len(nums) // 3

nums_count = Counter(nums).most_common()

ans = []


for item in nums_count:
    if item[1] > b:
        ans.append(item[0])

print(ans)