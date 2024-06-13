# https://leetcode.com/problems/majority-element/

from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        x = Counter(nums)
        
        answer, *v = x

        return answer
