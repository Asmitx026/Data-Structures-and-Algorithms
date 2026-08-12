class MinStack:
    '''
    Using a min integer to track the min value plus storing encoded (difference between min and the value) values in the stack
    Leads to simple 0(1) time complexity for the getMin() function
    '''

    def __init__(self):
        self.stack = []
        self.min = float('inf')

    def push(self, value: int) -> None:
        if not self.stack:
            self.min = value
            self.stack.append(0)
            return

        self.stack.append(value - self.min)
        if self.min > value:
            self.min = value

    def pop(self) -> None:
        if not self.stack:
            return
        pop = self.stack.pop()
        
        if pop < 0:
            self.min = self.min - pop

    def top(self) -> int:
        if not self.stack:
            return
        top = self.stack[-1]

        if top < 0:
            return self.min
        else:
            return top + self.min

    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()