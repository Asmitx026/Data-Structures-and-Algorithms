class Solution:
    def isValid(self, s: str) -> bool:
        '''
        using Stack
        '''
        seen = []

        for char in s:
            if char == '(' or char == '{' or char == '[':
                seen.append(char)
            else:
                if len(seen) == 0:
                    return False

                top = seen.pop()
                if char == ')' and top != '(':
                    return False
                elif char == '}' and top != '{':
                    return False
                elif char == ']' and top != '[':
                    return False
            
        return len(seen) == 0