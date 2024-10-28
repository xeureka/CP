# https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/description/?envType=problem-list-v2&envId=counting

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if (i < j) and (abs(nums[i] - nums[j]) == k):
                    count += 1
        
        return count



        
        