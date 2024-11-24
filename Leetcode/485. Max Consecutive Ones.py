# https://leetcode.com/problems/max-consecutive-ones/description/

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current_count=max_count = 0

        for num in nums:
            if num == 1:
                current_count += 1
            
            else:
                max_count = max(current_count,max_count)
                current_count = 0
        
        return max(current_count,max_count)
        