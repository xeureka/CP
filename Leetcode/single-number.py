# https://leetcode.com/problems/single-number/description/


from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        values = Counter(nums)

        ans = []

        for i in values:
            if values[i] ==1:
                ans.append(i)
                break
            
        return ans[0]