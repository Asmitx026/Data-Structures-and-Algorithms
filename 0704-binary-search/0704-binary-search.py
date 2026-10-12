class Solution:
    def search(self, nums: list[int], target: int) -> int:
        '''
        using Iterative Binary Search approach, leads to O(logN) time and O(1) space complexity
        better than recursive approach for space complexity
        '''

        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (end + start) // 2

            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        
        return -1