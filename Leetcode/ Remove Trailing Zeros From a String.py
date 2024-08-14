# https://leetcode.com/problems/remove-trailing-zeros-from-a-string/description/


class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        return num.rstrip('0')
        

