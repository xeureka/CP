# https://leetcode.com/problems/majority-element/

from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        most = counter.most_common(1)

        return most[0][0]
