# https://leetcode.com/problems/add-binary/description/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        summ = bin(int(a,2) + int(b,2))

        final = summ[2:]
        return str(final)
        