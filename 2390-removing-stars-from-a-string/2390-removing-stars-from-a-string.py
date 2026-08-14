class Solution:
    def removeStars(self, s: str) -> str:
        '''
        Simple Stack-based implementation with O(n) time complexity but o(n) space complexity
        '''

        stack = []
        for ch in s:
            if ch == '*':
                # if stack: - not required since its said that the op is always possible
                stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)