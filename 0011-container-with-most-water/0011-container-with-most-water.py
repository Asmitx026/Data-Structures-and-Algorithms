class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        max_area = 0
        left, right = 0, n - 1

        while left < right:
            curr_width = right - left
            curr_height = min(height[left],height[right])
            curr_area = curr_width * curr_height

            max_area = max(max_area, curr_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area