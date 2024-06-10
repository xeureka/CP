# https://leetcode.com/problems/missing-number/description/
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        s = set(nums)

        for num in range(n+1):
            if num not in s:
                return num