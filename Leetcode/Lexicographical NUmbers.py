# https://leetcode.com/problems/lexicographical-numbers/

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = [str(i) for i in range(1,n+1)]
        ans.sort()
        return [int(j) for j in ans]
        