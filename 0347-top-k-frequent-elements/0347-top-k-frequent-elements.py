class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        using HashMaps, reverse sorting the key-val pairs and putting the keys in another list
        Simple but higher time complexity: O(n*nlogn)
        '''

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
        '''
        
        '''
        using HashMap and Bucket Sort (storing in buckets of frequencies of occurence)
        Doesn't requires sorting, so has a time complexity of O(n) (O(n+m+k))
        '''

        count = {}
        buckets = [[] for _ in range(len(nums)+1)]

        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1
        
        for num, count in count.items():
            buckets[count].append(num)

        res = []
        while len(res) < k:
            val = buckets.pop()
            if not val:
                continue
            for num in val:
                res.append(num)

        return res
