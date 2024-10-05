# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        n = len(nums) 

        for num in nums:
            inn = abs(num) - 1
            nums[inn] = -abs(nums[inn])
        
        return [i+1 for i in range(n) if nums[i] > 0]
        