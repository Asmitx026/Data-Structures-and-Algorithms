class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        '''
        SImple hashmap implementation, leads to O(N) time and space complexity
        '''
        seen = {}
        res = 0

        for num in nums:
            if num not in seen:
                seen[num] = 0
            seen[num] += 1
        
        for num,count in seen.items():
            if count > len(nums) / 2:
                res = num
                break

        return res