# https://leetcode.com/problems/power-of-three/description/
import math

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        else:
            return(math.ceil(math.log10(n)/math.log10(3))==math.floor(math.log10(n)/math.log10(3)))

        