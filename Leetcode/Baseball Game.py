# https://leetcode.com/problems/baseball-game/description/

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans = []

        for i in operations:
            if i == 'D':
                new = int(ans[-1])
                ans.append(2*new)
            elif i == 'C':
                ans.pop(-1)
            elif i == '+':
                summ = int(ans[-2]) + int(ans[-1])
                ans.append(summ)
            else:
                ans.append(int(i))
        return sum(ans)