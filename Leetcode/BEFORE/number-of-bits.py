# https://leetcode.com/problems/number-of-1-bits/description/

class Solution:
    def hammingWeight(self, n: int) -> int:
        count=0
        while(n>0):
            if(n%2==1):
                count+=1
            n=n//2
        return count
        