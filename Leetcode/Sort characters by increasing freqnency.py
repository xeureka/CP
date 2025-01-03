# https://leetcode.com/problems/sort-characters-by-frequency/description/?source=submission-noac

from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        cnt = Counter(s)

        return ''.join(c * v for c, v in sorted(cnt.items(), key=lambda x: -x[1]))
        