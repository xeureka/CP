# https://leetcode.com/problems/majority-element-ii/description/


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        b = len(nums) // 3
        nums_count = Counter(nums).most_common()

        ans = []

        for item in nums_count:
            if item[1] > b:
                ans.append(item[0])
        
        return ans