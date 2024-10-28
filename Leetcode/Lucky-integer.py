# https://leetcode.com/problems/find-lucky-integer-in-an-array/description/?envType=problem-list-v2&envId=counting

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        lucky = []

        for i in arr:
            if i == arr.count(i):
                lucky.append(i)
        
        if len(lucky) >= 1:
            return max(lucky)
        return -1
        