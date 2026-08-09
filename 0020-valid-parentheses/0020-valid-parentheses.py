class Solution:
    def isValid(self, s: str) -> bool:
        '''
        using Stack and a HashMap of paranthesis
        '''

        seen = []
        brackets = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:
            if char in brackets:
                if len(seen) == 0 or seen.pop() != brackets[char]:
                    return False
            else:
                seen.append(char)

        return len(seen) == 0