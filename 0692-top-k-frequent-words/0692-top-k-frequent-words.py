class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        '''
        using HashMap + Max-Heap (min-heap * -1 to simulate that), leads to O() time and space complexity
        '''

        seen = {}
        heap = []
        res = []

        for word in words:
            if word not in seen:
                seen[word] = 0
            seen[word] += 1
        
        for word,count in seen.items():
            heapq.heappush(heap, (-count,word))
            
        while k > 0:
            res.append(heapq.heappop(heap)[1])
            k -= 1

        return res