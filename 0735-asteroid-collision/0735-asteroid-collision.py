class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        '''
        Simple Stack Implementation, leads to O(N) time and space complexity
        '''

        stack = []
        
        for num in asteroids:
            if not stack:
                stack.append(num)
                continue

            while stack and num < 0 < stack[-1]:
                # since collision occurs only when an asteroid (stack top) is moving towards right (positive) and the next one (num) is moving towards left (negative)
                if stack[-1] < -num:
                    stack.pop()
                elif stack[-1] == -num:
                    stack.pop()
                    break
                else:
                    break
            else:
                stack.append(num)

        return stack
                
                