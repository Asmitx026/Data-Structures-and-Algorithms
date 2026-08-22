class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        3-Pointer Approach (Dutch National Flag)
        """
        
        start, mid = 0, 0
        end = len(nums) - 1
        while mid <= end:
            if nums[mid] == 0:
                nums[mid], nums[start] = nums[start], nums[mid]
                start += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[end] = nums[end], nums[mid]
                end -= 1

        """
        Do not return anything, modify nums in-place instead.
        overwirtting the array via Hashmaps
        """
        """
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        idx, col = 0, 0
        while idx < len(nums):
            freq = count.get(col, 0)
            nums[idx:idx+freq] = [col] * freq
            idx += freq
            col += 1
        
        return nums
        """