# https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:

        left,right = 0,1

        while right < len(nums):
            if nums[left] == nums[right]:
                nums[left] *= 2
                nums[right] = 0

            left += 1
            right += 1
        
        idx = 0

        for current,value in enumerate(nums):
            if value != 0:
                nums[idx],nums[current] = nums[current],nums[idx]
                idx += 1

        
        
        return nums
        