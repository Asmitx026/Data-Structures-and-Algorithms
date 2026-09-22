class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        '''
        Using hash set, leads to O(N) time and space complexity
        '''
        seen = set(nums)
        res = 0

        for num in seen:
            if num-1 not in seen:
                length = 1

                while num+length in seen:
                    length += 1
                    
                res = max(length, res)

        return res