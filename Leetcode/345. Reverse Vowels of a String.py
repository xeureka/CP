
# https://leetcode.com/problems/reverse-vowels-of-a-string/

class Solution:
    def reverseVowels(self, s: str) -> str:
            s = list(s)

            left,right = 0,len(s) -1

            vow = ['a', 'e', 'i', 'o', 'u']

            while left <= right:
                if (s[left].lower() in vow) and (s[right].lower() in vow):
                    s[left],s[right] = s[right],s[left]
                    left += 1
                    right -= 1
                
                elif not s[left].lower() in vow:
                    left += 1
                
                else:
                    right -= 1
            
            return ''.join(s)
        