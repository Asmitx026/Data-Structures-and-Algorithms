class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        Follow-Up Approach: 'Can you solve the problem in O(1) space complexity?'
        Optimized Prefix-Suffix Approach - creating the op list by appending product of prefix elements of `nums` list, then doing multiplying the elements in `op` list with the product of the suffix elements of `nums` list in reverse loop 
        '''

        n = len(nums)
        op = []

        pf = 1
        for i in range(n):
            op.append(pf)
            pf *= nums[i]
        
        sf = 1
        for i in range(1,n+1):
            op[-i] *= sf
            sf *= nums[-i]
        
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