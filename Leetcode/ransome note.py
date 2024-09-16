# https://leetcode.com/problems/ransom-note/

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        countR,countM = Counter(ransomNote),Counter(magazine)

        if countR & countM == countR:
            return True
        return False
        