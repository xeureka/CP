# https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/


class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        for num in range(left,right + 1):
            count = 0
            for s, e in ranges:
                count = 1
                break
        if count ==0 :
            return False
        return True