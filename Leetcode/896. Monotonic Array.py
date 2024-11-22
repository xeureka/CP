# https://leetcode.com/problems/monotonic-array/description/


from typing import *


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:

        def up_mono(nums:list):
            left,right = 0,1
            count = 0

            while right <= len(nums)-1:
                if (nums[left] <= nums[right]):
                    left += 1
                    right += 1

                else:
                    return False
            return True

        def down_mono(nums:list):
            left,right = 0,1

            while right <= len(nums) - 1:
                if nums[left] >= nums[right]:
                    left += 1
                    right += 1
                else:
                    return False
            
            return True
        
        if up_mono(nums) or down_mono(nums):
            return True
        
        return False
                
        