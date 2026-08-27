class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = []
            for j in range(9):
                num = board[i][j]
                if num != ".":
                    if num in row:
                        return False
                    row.append(num)
        
        for i in range(9):
            col = []
            for j in range(9):
                num = board[j][i]
                if num != ".":
                    if num in col:
                        return False
                    col.append(num)

        for i in range(0,9,3):
            for j in range(0,9,3):
                box = []

                for x in range(i,i+3):
                    for y in range(j,j+3):
                        num = board[x][y]
                        if num != ".":
                            if num in box:
                                return False
                            box.append(num)
        return True