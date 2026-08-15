class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        Follow-Up Approach: 'Can you solve the problem in O(1) space complexity?'
        Optimized Prefix-Suffix Approach - creating the prefix list, then multiplying the elements in that list (reverse loop) with the product of the suffix elements (while storing the product with each iterating in `sf`)
        '''

        n = len(nums)
        op = [1]*n

        for i in range(1,n):
            op[i] = nums[i-1] * op[i-1]
        
        sf = 1
        for i in range(2,n+1):
            sf *= nums[-i+1]
            op[-i] *= sf
        
        return op

        '''
        Prefix-Suffix Approach - O(n) time complexity but requires extra space O(N) excl. output list
        '''

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
        '''