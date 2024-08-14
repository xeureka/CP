# https://leetcode.com/problems/buy-two-chocolates/


class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()

        summ = prices[0] + prices[1]

        if money - summ < 0:
            return money
        elif summ > money:
            return money
        else:
            return money - summ
            
        