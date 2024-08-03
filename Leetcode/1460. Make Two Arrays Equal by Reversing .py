# https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/description/

class Solution(object):
    def canBeEqual(self, target, arr):
        arr.sort()
        target.sort()

        for i in range(len(arr)):
            if arr[i] != target[i]:
                return False
        return True
        