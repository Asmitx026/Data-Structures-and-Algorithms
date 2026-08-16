class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        '''
        Multiple other ways to solve this problem: 
        - Extend method
        - + & * operator
        - Using loop and appending the values to a shallow copy (`ans`) 
            (logical way to 'Return the array `ans`' but takes auxillary space)
        '''

        return nums*2 # most efficient way in terms of runtime and memory space

        # return nums+nums
        # nums.extend(nums); return nums
        # ans=nums.copy();for num in nums:;ans.append(num);return ans