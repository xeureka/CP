# https://leetcode.com/problems/number-complement/description/


class Solution:
    def findComplement(self, num: int) -> int:
        bin_num = bin(num)
        value = str(bin_num[2:])

        ans = ''

        for i in value:
            if i == '1':
                ans += '0'
            else:
                ans += '1'
        return int(ans,2)
        