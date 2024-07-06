# https://leetcode.com/problems/valid-palindrome/description/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == " ":
            return True
        
        else:
            s = s.lower()
            s.replace(" ","")

            def letters(input):
                return ''.join(filter(str.isalpha,input))
            new = letters(s)

            rev = new[::-1]