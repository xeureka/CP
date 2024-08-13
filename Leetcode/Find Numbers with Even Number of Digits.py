# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/description/

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = [i for i in nums if len(str(i)) % 2 ==0]

        return len(count)