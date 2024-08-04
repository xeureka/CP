import copy

class Solution(object):
    def productExceptSelf(self, nums):
        
        def pro(num):
            pro = 1
            for i in num:
                pro *= i
            return pro
        
        ans = []
        new = copy.deepcopy(nums)

        for i in nums:
            new.remove(i)
            ans.append(pro(new))
            new = copy.deepcopy(nums)
        
        return ans
        