# https://leetcode.com/problems/isomorphic-strings/description/


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:


            if len(s) != len(t):
                return False
            sStack,tStack = [],[]

            for i in range(len(s)):
                sStack.append(s.index(s[i]))
                
                tStack.append(t.index(t[i]))
            
            return sStack == tStack
        