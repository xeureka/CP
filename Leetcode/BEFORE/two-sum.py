# https://leetcode.com/problems/two-sum/description/

from typing import *

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left,right = 0,len(nums) - 1

        while left < right:
            
            current_sum = nums[left] + nums[right]

            if current_sum == target:
                
                return [left + 1,right +1]

            elif current_sum < target:
                left += 1
            else:
                right -= 1

