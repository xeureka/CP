# https://leetcode.com/problems/find-if-digit-game-can-be-won/description/

class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        alice_s = [i for i in nums if i < 10]
        alice_d = [i for i in nums if i >= 10]

        bob_s = sum(nums) - sum(alice_s)
        bob_d = sum(nums) - sum(alice_d)

        if (sum(alice_s) > bob_s) or (sum(alice_d) > bob_d):
            return True
        return False
        