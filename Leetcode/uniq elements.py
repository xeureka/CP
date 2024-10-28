# https://leetcode.com/problems/sum-of-unique-elements/description/

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        uniq_sum = 0

        for i in nums:
            if nums.count(i) == 1:
                uniq_sum += i
        return uniq_sum
        