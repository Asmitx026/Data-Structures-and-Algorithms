class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        '''
        Basically this approach iterating the combination of i and j, and then finding the other two numbers using the classic two-sum way (two-pointer approach)

        Leads to O(N**3) time and O(N) space, so dont worry about optimizing for logarithmic times when solving professionally
        '''
        
        nums.sort()
        res = []

        n = len(nums)
        i = 0

        while i < n:
            j = 1 + i

            while j < n:
                left, right = j + 1, n - 1
                goal = target - nums[i] - nums[j]
                
                while left < right:
                    if nums[left] + nums[right] < goal:
                        left += 1
                    elif nums[left] + nums[right] > goal:
                        right -= 1
                    else:
                        res.append([nums[i],nums[j],nums[left],nums[right]])
                        while left + 1 < n and nums[left] == nums[left + 1]:
                            left += 1

                        left += 1
                        right -= 1

                while j + 1 < n and nums[j] == nums[j + 1]:
                    j += 1
                j += 1

            while i + 1 < n and nums[i] == nums[i + 1]:
                i += 1
            i += 1
        
        return res