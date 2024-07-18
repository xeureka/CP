
# https://leetcode.com/problems/third-maximum-number/description/

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        else:
            ans = set(nums)
            ans = list(ans)

            if len(ans) <= 2:
                return max(ans)
            else:
                for i in range(2):
                    ans.remove(max(ans))
                return max(ans)
            

            