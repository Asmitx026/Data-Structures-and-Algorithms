class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        using Sliding Window approach, results in O(n) time and O(1) space complexity
        '''

        left = max_len = 0
        window = set()
        
        for right in range(len(s)):
            while s[right] in window:
                window.remove(s[left])
                left += 1
            curr_len = (right - left) + 1

            window.add(s[right])
            max_len = max(max_len, curr_len)
        
        return max_len