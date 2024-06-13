# https://leetcode.com/problems/majority-element-ii/description/

from collections import Counter
nums = [1,2,3,4,5]

counter = Counter(nums)
most = counter.most_common()
print(most)
