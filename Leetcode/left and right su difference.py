# https://leetcode.com/problems/left-and-right-sum-differences/description/

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        def rightSum(num):
            ans = []
            total_sum = 0

            for i in range(len(num)-1, -1, -1):
                total += num[i]
                ans.append(total)

            return ans[::-1]


        def leftSum(num):
            ans = []
            total = 0

            for i in range(len(num)):
                total += num[i]
                ans.append(total)

            return ans
        
        lst = list(zip(leftSum(nums),rightSum(nums)))

        answer = []

        for i in lst:
            fi = abs(i[0] - i[1])
            answer.append(fi)

        return answer