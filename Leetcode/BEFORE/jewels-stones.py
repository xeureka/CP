# https://leetcode.com/problems/jewels-and-stones/

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        cout = 0

        for i in stones:
            if i in jewels:
                cout +=1

        return cout