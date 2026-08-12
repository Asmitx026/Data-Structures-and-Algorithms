class MinStack:
    '''
    [DISCARDED cuz too complex for a simple problem]
    Using a min integer to track the min value plus storing encoded (difference between min and the value) values in the stack
    Leads to simple 0(1) time complexity for the getMin() function
    '''

    '''
    Using two stacks, one to store the elements and one to store the min. numbers (not all elements in the stack tho)
    Simpler plus O(1) time complexity but high space complexity ((O(n+m))
    NOTE: min stack stores only the elements smaller than its predecessors
    '''

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, value: int) -> None:
        if not self.stack:
            self.min.append(value)
        else:
            if self.min[-1] >= value:
                self.min.append(value)
        self.stack.append(value)

    def pop(self) -> None:
        if self.stack:
            pop = self.stack.pop()
            if self.min[-1] == pop:
                self.min.pop()
        
    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()