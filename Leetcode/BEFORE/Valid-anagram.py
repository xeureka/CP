# https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cout = len(s)
        if len(s) == len(t):
            for i in s:
                if i in t:
                    cout -=1
            if cout ==0:
                return True
            else:
                return False
        else:
            return False



