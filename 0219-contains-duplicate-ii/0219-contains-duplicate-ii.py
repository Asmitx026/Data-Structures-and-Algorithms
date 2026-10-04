class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        '''
        Using the classic sliding window set approach.. leads to O(N) time and space complexity
        '''
        window = set()

        for i,val in enumerate(nums):
            if i > k:
                window.remove(nums[i-k-1])

            if val in window:
                return True
            window.add(val)
        
        return False