class Solution(object):
    def findGCD(self, nums: int) -> list[int]:
        '''
        Using the Euclidean algorithm, leads to O(n+logn) time complexity
        '''
        mn, mx = 1000, 1
        for num in nums:
            if num < mn:
                mn = num
            if mx < num:
                mx = num
        
        while mx!=0:
            mn, mx = mx, mn%mx
        return mn