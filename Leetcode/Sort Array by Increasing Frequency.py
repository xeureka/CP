# https://leetcode.com/problems/sort-array-by-increasing-frequency/description/


from collections import Counter


class Solution(object):
    def frequencySort(self, nums):
        num = Counter(nums)

        def sorter(n):
            return (num[n],-n)

        nums.sort(key=sorter)

        return nums