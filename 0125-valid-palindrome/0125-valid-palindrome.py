class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        via Two Pointers
        '''
        
        s = ''.join(char.lower() for char in s if char.isalnum())
        # return s == s[::-1] # even simpler approach to this problem

        i, j = 0, len(s)-1
        while i < j:
            if s[i] != s[j]:
                return False

            i += 1
            j -= 1
        return True