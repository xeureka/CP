# https://leetcode.com/problems/merge-sorted-array/description/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1.extend(nums2)
        nums1.sort()

        if len(nums1) > (m + n):
            while len(nums1) != (n + m):
                nums1.remove(0)
        return nums1
        

        