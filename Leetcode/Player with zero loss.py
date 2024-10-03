# https://leetcode.com/problems/find-players-with-zero-or-one-losses/description/


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loss_count = defaultdict(int)

        winners = set()

        for winner,loser in matches:
            winners.add(winner)
            loss_count[loser] += 1

        no_loss = sorted([i for i in winners if loss_count[i] == 0])
        one_loss = sorted([i for i,count in loss_count.items() if count == 1])

        return [no_loss,one_loss]