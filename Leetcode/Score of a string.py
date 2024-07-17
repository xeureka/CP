
# https://leetcode.com/problems/score-of-a-string/description/

class Solution:
    def scoreOfString(self, s: str) -> int:
        cout = 0
        asc = []
        for i in s:
            asc.append(ord(i))

        for i in range(len(asc)):
            try:
                cout += abs(asc[i] - asc[i+1])
            except:
                break
        return cout