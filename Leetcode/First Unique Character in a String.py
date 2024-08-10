# https://leetcode.com/problems/first-unique-character-in-a-string/description/


from collections import Counter

class Solution:
    def firstUniqChar(self,s:str) -> int:
        
        new = Counter(list(s))

        for i,j in new.items():
            
            if j == 1:
                return s.index(i)
        return -1
        

            