class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        using HashMaps, reverse sorting the key-val pairs and putting the keys in another list
        Simple but higher time complexity: O(n*nlogn)
        '''
        words = {}
        for num in nums:
            if num not in words:
                words[num] = 0
            words[num] += 1
        
        op = []
        for key, val in words.items():
            op.append([val,key])
        op.sort(reverse=True)

        res = []
        for i in range(k):
            res.append(op[i][1])

        return res