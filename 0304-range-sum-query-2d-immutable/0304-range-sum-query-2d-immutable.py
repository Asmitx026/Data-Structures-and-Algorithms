class NumMatrix:
    '''
    using 2D Prefix Sum approach to solve.. leads to O(mn) space and O(1) time complexity
    '''

    def __init__(self, matrix: list[list[int]]):
        rows = len(matrix)
        cols = len(matrix[0])
        self.prefix = [[0 for _ in range(cols)] for _ in range(rows)]

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                self.prefix[row][col] = matrix[row][col]

                if row > 0:
                    self.prefix[row][col] += self.prefix[row - 1][col]

                if col > 0:
                    self.prefix[row][col] += self.prefix[row][col - 1]
                
                if row > 0 and col > 0:
                    self.prefix[row][col] -= self.prefix[row - 1][col - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = self.prefix[row2][col2]

        if row1 > 0:
            sum -= self.prefix[row1 - 1][col2]
        
        if col1 > 0:
            sum -= self.prefix[row2][col1 - 1]

        if row1 > 0 and col1 > 0:
            sum += self.prefix[row1 - 1][col1 - 1]

        return sum

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)