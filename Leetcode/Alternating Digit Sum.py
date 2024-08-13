# https://leetcode.com/problems/alternating-digit-sum/description/


class Solution:
    def alternateDigitSum(self, n: int) -> int:
        n = str(n)
        ans = 0

        for i in range(0,len(n)):
            val = int(n[i])
            if (i ==0) or (i % 2 ==0):
                ans += val
            else:
                ans += -val

        return ans