# https://leetcode.com/problems/first-letter-to-appear-twice/description/


class Solution:
    def repeatedCharacter(self, s: str) -> str:
        repeat = []

        for i in s:
            if not i in repeat:
                repeat.append(i)
            else:
                return i
        