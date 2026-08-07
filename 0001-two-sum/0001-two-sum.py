class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i,digit in enumerate(nums):
            complement = target - digit
            if complement in seen and seen[complement] != i:
                return [seen[complement],i]
            seen[digit] = i