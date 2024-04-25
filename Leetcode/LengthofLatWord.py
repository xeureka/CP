# https://leetcode.com/problems/length-of-last-word/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        w = " ".join(s.split())
        rev = s[::-1]

        new = ' '
        for i in rev:
            if not i.isspace():
                new +=i
            else:
                break
        return len(new.strip())