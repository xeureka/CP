# https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/


class Solution(object):
    def isCovered(self, ranges, left, right):
        covered_range = set()

        for start,end in ranges:
            for num in range(start,end + 1):
                covered_range.add(num)

        for num in range(left,right+1):
            if num not in covered_range:
                return False
            
        return True