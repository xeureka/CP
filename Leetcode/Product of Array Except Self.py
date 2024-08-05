# https://leetcode.com/problems/product-of-array-except-self/

from copy import deepcopy as dp

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        def pro(num):
            pro = 1
            for i in num:
                pro *= i
            return pro

        nn = pro(nums)
        ans = []

        for i in nums:
            try:
                val = nn / i
                ans.append(int(val))
            except:
                new = dp(nums)
                new.remove(i)
                ans.append(pro(new))
        return ans
        
        