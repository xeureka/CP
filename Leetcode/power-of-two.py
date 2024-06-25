# 


import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if(n==0 or n<0):
            return False
        else:
            return(math.ceil(math.log10(n)/math.log10(2))==math.floor(math.log10(n)/math.log10(2)))
        