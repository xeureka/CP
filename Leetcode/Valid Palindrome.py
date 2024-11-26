# https://leetcode.com/problems/valid-palindrome/


class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = []

        for i in s:
            if i.isalnum():
                word.append(i.lower())
            
        left,right = 0,len(word) - 1

        while left <= right:
            if word[left] != word[right]:
                return False
            else:
                left += 1
                right -= 1
        
        return True
        
        