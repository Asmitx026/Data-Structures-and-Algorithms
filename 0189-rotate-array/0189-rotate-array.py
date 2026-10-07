class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        Simple Three-Pointer approach, first reversing the whole array (0 to n) to bring the final k elements to front, then reversing them (0 to k-1) and reversing the rest of the remaining ones (k to n)
        """
        
        k = k % len(nums)

        start, end = 0, len(nums) - 1
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

        start, end = 0, k-1
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
        
        start, end = k, len(nums) - 1
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1