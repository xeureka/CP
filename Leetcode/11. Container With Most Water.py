
# https://leetcode.com/problems/container-with-most-water/description/


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left,right = 0,len(height) -1
        max_area = 0

        while left < right:
            width = right - left

            area = min(height[left] , height[right]) * width
            max_area = max(area,max_area)

            if height[left] < height[right]:
                left += 1

            else:
                right -= 1
        return max_area 
        
        