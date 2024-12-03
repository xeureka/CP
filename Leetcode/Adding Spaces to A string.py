# https://leetcode.com/problems/adding-spaces-to-a-string/description/

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:

        result = []
        index = 0

        for i in range(len(s)):
            if index < len(spaces) and i == spaces[index]:
                result.append(' ')
                index += 1

            result.append(s[i])

        return ''.join(result)
            