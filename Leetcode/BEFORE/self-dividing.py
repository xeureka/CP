# https://leetcode.com/problems/self-dividing-numbers/


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        
        def div(self,n):
            for i in n:
                i = int(i)
                n = int(n)

                if n % i ==0:
                    cout +=1
            n = str(n)

            if cout == len(n):
                return True
            else:
                return False

        for i in range(left,right+1):
            
        