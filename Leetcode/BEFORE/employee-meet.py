# https://leetcode.com/problems/number-of-employees-who-met-the-target/description/

class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        cout = 0
        for i in hours:
            if i >= target:
                cout +=1
        return cout