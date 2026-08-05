class Solution(object):
    def sortArray(self, nums):
        """
        Randomized Quick Sort
        :type nums: List[int]
        :rtype: List[int]
        """

        return self.quickSort(nums)

    def quickSort(self, nums):
        if len(nums) <= 1:
            return nums

        pivot = random.choice(nums)
        lt, rt, eq = [], [], []

        for num in nums:
            if num < pivot:
                lt.append(num)
            elif num == pivot:
                eq.append(num)
            else:
                rt.append(num)

        return self.quickSort(lt) + eq + self.quickSort(rt)