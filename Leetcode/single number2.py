# https://leetcode.com/problems/single-number-ii/description/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        number = Counter(nums)

        for i,j in number.items():
            if j == 1:
                return i
