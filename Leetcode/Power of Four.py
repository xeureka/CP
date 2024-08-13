# https://leetcode.com/problems/power-of-four/description/
import math

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        else:
            return(math.ceil(math.log10(n)/math.log10(4))==math.floor(math.log10(n)/math.log10(4)))