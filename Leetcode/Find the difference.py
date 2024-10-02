# https://leetcode.com/problems/find-the-difference/description/


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if len(s) == 0:
            return t[0]
        
        for i in range(len(s)):
            t = t.replace(s[i],'',1)

        return t
        