# https://leetcode.com/problems/squares-of-a-sorted-array/description/


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = sorted(map(lambda x:x**2,nums))
        return ans
        