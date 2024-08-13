# https://leetcode.com/problems/find-all-duplicates-in-an-array/description/


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        count = Counter(nums)

        ans = []

        for i,j in count.items():
            if j == 2:
                ans.append(i)
        return ans