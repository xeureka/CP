# https://leetcode.com/problems/special-array-i/description/


class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
            def parity(num):
                return num % 2 == 0
            
            if len(nums) == 1:
                return True
            
            left,right = 0,1

            while right <= len(nums) - 1:
                if parity(nums[left]) == parity(nums[right]):
                    return False
                
                left += 1
                right += 1
            
            return True
        