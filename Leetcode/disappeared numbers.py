# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        maxVal = max(nums)
        minVal = min(nums)
        result = []

        if len(nums) ==2 and (minVal == maxVal):
            if minVal == 1:
                return [minVal + 1]
            else:
                return [minVal - 1]

        elif (len(nums) == maxVal) or (maxVal > len(nums)):
            for i in range(minVal,maxVal + 1):
                if not i in nums:
                    result.append(i)
        
        else:
            for i in range(minVal,len(nums) + 1):
                if not i in nums:
                    result.append(i)
        return result

          
        