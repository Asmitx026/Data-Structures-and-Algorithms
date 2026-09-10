class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        '''
        Simple Two-Pointer approach with a static incrementing one
        O(n²) time complexity with O(1) space 
        (better than O(n) space complexity of HashMap approach)
        '''
        
        res = []
        n = len(nums)
        nums.sort()

        for i,num in enumerate(nums):
            if num > 0:
                break
            if i > 0 and num == nums[i-1]:
                # when num is same as previous (duplicate), skip it
                continue

            left, right = i+1, n-1
            while left < right:
                threeSum = num + nums[left] + nums[right]

                if threeSum == 0:
                    res.append([num,nums[left],nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left-1] and left < right:
                        # as long as the next 'left' number is same as previous (duplicate), it skips the left ptr
                        left += 1
                elif threeSum < 0:
                    left += 1
                else: # 0 < threeSum
                    right -= 1
        
        return res
