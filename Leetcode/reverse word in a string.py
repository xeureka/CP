# https://leetcode.com/problems/reverse-words-in-a-string/description/


class Solution:
    def reverseWords(self, s: str) -> str:
        lst = s.split()
        lst.reverse()
        
        ans = ''

        for i in lst:
            ans += ' '
            ans += i

        return ans.strip()
        