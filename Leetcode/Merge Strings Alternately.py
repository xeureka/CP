# https://leetcode.com/problems/merge-strings-alternately/description/


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        comb = ''
        cout = 0

        if len(word1) > len(word2):
            cout = len(word1)
            for i in range(cout):
                try:
                    comb += word1[i] + word2[i]
                except:
                    comb += word1[i]
        elif len(word1) < len(word2):
            cout = len(word2)

            for i in range(cout):
                try:
                    comb += word1[i] + word2[i]
                except:
                    comb += word2[i]
        else:
            cout = len(word1)

            for i in range(cout):
                comb += word1[i] + word2[i]
        return comb