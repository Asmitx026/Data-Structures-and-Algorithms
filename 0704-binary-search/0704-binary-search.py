class Solution:
    def search(self, nums: list[int], target: int) -> int:
        '''
        using Recursive Binary Search approach, leads to O(logN) time and space complexity
        '''
        def binSearch(start, end):
            if start > end:
                return -1

            mid = (end + start) // 2

            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                return binSearch(start, mid - 1)
            else:
                return binSearch(mid + 1, end)

        return binSearch(0, len(nums) - 1)