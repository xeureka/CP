# https://leetcode.com/problems/valid-parentheses/
from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()

        
        combined = {')':'(',
                    '}':'{',
                    ']':'['}

        for char in s:
            if not char in combined:
                stack.append(char)
            
            elif (char in combined)  and (len(stack) >0) and (combined[char] == stack[-1]) :
                stack.pop()
            else:
                return False
        
        return not stack
