class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        count = {}
        for char in s:
            try:
                count[char] += 1
            except KeyError:
                count[char] = 1
        
        for char in t:
            try:
                count[char] -= 1
            except KeyError:
                return False
        
        return True if all(v == 0 for v in count.values()) else False