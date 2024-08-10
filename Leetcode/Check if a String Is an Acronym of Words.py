# https://leetcode.com/problems/check-if-a-string-is-an-acronym-of-words/description/

class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        ans = ''

        for word in words:
            ans += word[0]
        return ans == s
        