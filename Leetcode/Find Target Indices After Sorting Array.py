# https://leetcode.com/problems/find-target-indices-after-sorting-array/description/


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        co = nums.count(target)
        
        ans = []

        for i in range(len(nums)):
            if nums[i] == target:
                ans.append(i)

                if len(ans) == co:
                    break
        return ans
            

        