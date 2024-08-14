# https://leetcode.com/problems/shuffle-the-array/description/


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        first = nums[:n]
        second = nums[n:]

        
        ans = []

        for i in list(zip(first,second)):
            for j in i:
                ans.append(j)
        return ans
                    