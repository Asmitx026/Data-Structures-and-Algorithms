class Solution(object):
    def isAnagram(self, s: str, t: str) -> bool:
        """
        HashMap approach, leads to O(n) time complexity
        """
        
        if len(s) != len(t):
            return False
        count = {}

        for char in s:
            if char not in count:
                count[char] = 0
            count[char] += 1
        
        for char in t:
            if char not in count or count[char] == 0: # returns False if count of that char is already zero (since it'll then lead to negative int after decrement) or if char not a valid key
                return False
            count[char] -= 1
        
        return True