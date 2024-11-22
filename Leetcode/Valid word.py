# https://leetcode.com/problems/valid-word/description/


class Solution:
    def isValid(self, word: str) -> bool:
        vowel = set(['a', 'e', 'i', 'o', 'u'])
        c,v = 0,0

        if len(word) < 3:
            return False
        
        
        for char in word:
            if not char.isalnum():
                return False

            if not char.isdigit():
                if char.lower() in vowel:
                    v += 1
                
                else:
                    c += 1
        
        if c > 0 and v > 0:
            return True
        
        return False



        
                
        