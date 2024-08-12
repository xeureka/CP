# https://leetcode.com/problems/split-the-array/description/

class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:

        num = Counter(nums)

        for i in num.values():
            if i >2:
                return False
        return True
        