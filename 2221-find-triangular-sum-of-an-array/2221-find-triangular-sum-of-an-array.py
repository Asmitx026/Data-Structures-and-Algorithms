class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        newNums = []
        i = 0
        while len(newNums) < n-1:
            newNums.append((nums[i] + nums[i+1]) % 10)
            i += 1

        return self.triangularSum(newNums)