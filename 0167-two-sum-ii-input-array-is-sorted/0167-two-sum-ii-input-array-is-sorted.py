class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        Two Pointers Approach, with O(1) space
        '''

        start, end = 0, len(numbers) - 1
        while start < end:
            tot = numbers[start] + numbers[end]
            if tot > target:
                end -= 1
            elif tot < target:
                start += 1
            else:
                return [start+1, end+1]
        
        '''
        Same approach to TwoSum I with HashMap, although requires O(N) space complexity
        '''
        '''
        seen = {}

        for i, num in enumerate(numbers):
            comp = target - num
            if comp in seen:
                return [seen[comp]+1, i+1]
            seen[num] = i
        '''
                