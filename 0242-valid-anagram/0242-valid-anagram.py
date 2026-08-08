class Solution(object):
    def isAnagram(self, s, t):
        """
        via HashMap
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if len(s) != len(t):
            return False

        count = {}

        for char in s:
            if char not in count:
                count[char] = 0
            count[char] += 1
        
        for char in t:
            if char not in count:
                return False
            count[char] -= 1
        
        return all(v == 0 for v in count.values())