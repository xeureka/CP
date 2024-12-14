# https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/description/


class Solution:
    def findMaxK(self, nums: List[int]) -> int:

        if max(nums) and -max(nums) in nums:
            return max(nums)
        
        num = []
        
        for i in nums:
            if -i in nums:
                num.append(i)
        
        if len(num) > 0:
            return max(num)
        
        return -1
        