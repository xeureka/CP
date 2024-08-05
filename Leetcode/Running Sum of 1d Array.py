
# https://leetcode.com/problems/running-sum-of-1d-array/

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        sum = nums[0]

        for i in range(len(nums)):
            if i ==0:
                ans.append(sum)
            else:
                sum += nums[i]
                ans.append(sum)

        return ans
    
    


        