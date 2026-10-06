class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        Simple Two-Pointer approach, leads to O(N) time and O(1) space complexity.

        [also possible using recursion, stack and just using reverse()]
        """

        start, end = 0, len(s) - 1
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
