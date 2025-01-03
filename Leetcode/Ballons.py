# https://leetcode.com/problems/maximum-number-of-balloons/description/

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        ballon = 'balloon'

        counter = defaultdict(int)

        for i in text:
            if i in ballon:
                counter[i] += 1
        
        if any(c not in counter for c in ballon):
            return 0
        
        return min(counter['b'],counter['a'],counter['l'] // 2,counter['o'] // 2,counter['n'])
