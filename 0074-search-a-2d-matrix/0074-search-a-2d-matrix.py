class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        '''
        using Simple Binary Sort (considering the 2D array as a flattened 1D array)
        '''
        m, n = len(matrix), len(matrix[0])
        start = 0
        end = m * n - 1
        
        while start <= end:
            mid = (start + end) // 2
            row, col = mid // n, mid % n
            num = matrix[row][col]
            
            if target == num:
                return True
            elif num < target:
                start = mid + 1
            else:
                end = mid - 1
        
        return False