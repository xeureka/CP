# https://leetcode.com/problems/count-primes/description/

class Solution:
    def checkPrime(self,n):
        prime = True

        for i in range(2,n):
            if n % i ==0:
                prime = False
                break
        return prime


    def countPrimes(self, n: int) -> int:
        cout = 0

        for i in range(2,n):
            if self.checkPrime(i):
                cout +=1

        return cout
        