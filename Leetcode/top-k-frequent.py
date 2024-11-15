# https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = dict(Counter(nums))

        freq = {k:v for k,v in sorted(freq.items(),key= lambda item:item[1],reverse=True)}

        result = []
        i = 0

        for num,count in freq.items():
            result.append(num)
            i += 1
            if i == k:
                break
        
        return result