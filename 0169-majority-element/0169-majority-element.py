class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        '''
        The Moore Voting Approach: assumes the majority element will always remain in the lead
        leads to O(N) time and no extra space (O(1))
        '''

        res, majority = 0, 0

        for num in nums:
            if majority == 0:
                res = num
            
            if res == num:
                majority += 1
            else:
                majority -= 1

        return res

        '''
        SImple hashmap implementation, leads to O(N) time and space complexity
        '''
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
        '''