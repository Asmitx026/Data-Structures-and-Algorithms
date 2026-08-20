class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        overwirtting the array via Hashmaps
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