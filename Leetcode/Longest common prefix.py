# https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        for i ,group in enumerate(zip(*strs)):
            if len(set(group)) > 1:
                return strs[0][:i]
        else:
            return min(strs)


        