# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/description/

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        ans = 0

        for i in operations:
            if i == 'X++' or i == '++X':
                ans += 1
            elif i == 'X--' or '--X':
                ans -= 1
        return ans