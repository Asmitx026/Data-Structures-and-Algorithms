class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        '''
        Solved via applying the Pascal Triangle (binomial coefficient)
        Used the relation: C(n,k) = (C(n,k-1) × (n−k−1)) / k
        '''

        n = len(nums)
        if n == 1:
            return nums[0]

        c, res = 1, 0
        for i in range(n):
            res += nums[i] * c
            c = (c * (n-1-i)) // (i+1)

        return res % 10

        '''
        Solved via Recursion, simple but high time and space complexity, i.e., O(n²)
        '''

        '''
        n = len(nums)
        if n == 1:
            return nums[0]
        
        newNums = []
        i = 0
        while len(newNums) < n-1:
            newNums.append((nums[i] + nums[i+1]) % 10)
            i += 1

        return self.triangularSum(newNums)
        '''