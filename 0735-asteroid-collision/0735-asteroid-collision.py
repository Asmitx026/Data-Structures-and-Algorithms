class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []
        
        for num in asteroids:
            if len(stack) == 0:
                stack.append(num)
                continue
            
            num_positive = num > 0
            stack_positive = stack[-1] > 0

            if stack_positive and not num_positive:
                # since collision occurs only when an asteroid (stack top) is moving towards right (positive) and the next one (num) is moving towards left (negative)
                larger = False
                while stack_positive != num_positive and len(stack) != 0:
                    if abs(stack[-1]) < abs(num):
                        stack.pop()
                        larger = True
                    elif abs(stack[-1]) == abs(num):
                        stack.pop()
                        larger = False
                        break
                    else:
                        larger = False
                        break

                    stack_positive = stack[-1] > 0 if len(stack) != 0 else False
                
                if larger:
                    stack.append(num)
            else:
                stack.append(num)

        return stack
                
                