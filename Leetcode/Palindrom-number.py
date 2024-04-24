# https://leetcode.com/problems/palindrome-number/submissions/1241479352/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        rev = x[::-1]
        if x == rev:
            return True
        else:
            return False
        