# https://leetcode.com/problems/minimum-common-value/

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:

        try:
            return (min(set(nums1).intersection(set(nums2))))

        except:
            return (-1)
        