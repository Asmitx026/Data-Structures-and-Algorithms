class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        Prefix-Suffix Approach - O(n) time complexity but requires extra space O(N) excl. output list
        '''
        n = len(nums)
        pf, sf, op = [0]*n, [0]*n, [0]*n
        pf[0] = sf[-1] = 1

        for i in range(1,n):
            pf[i] = nums[i-1] * pf[i-1]
        for i in range(2, n+1):
            sf[-i] = sf[-i+1] * nums[-i+1]
        for i in range(n):
            op[i] = pf[i] * sf[i]

        return op