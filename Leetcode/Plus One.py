
# https://leetcode.com/problems/plus-one/

class Solution(object):
    def plusOne(self, digits):
        num = ''

        for i in digits:
            i = str(i)
            num += i

                
        lst = []

        for i in str(int(num) + 1):
            i = int(i)
            lst.append(i)
        
        return lst
        
        