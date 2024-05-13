class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        numRows = len(grid)#Rows
        numCols = len(grid[0])#Cols
        #Flip row if first num in that row is 0
        for i in range(numRows):
            if grid[i][0] == 0:
                #Flip the row
                for j in range(numCols):
                    grid[i][j] = 1 - grid[i][j]
        for m in range(1, numCols):
            zeroCount = 0
            for n in range(numRows):
                if grid[n][m] == 0:
                    zeroCount +=1
            if zeroCount > numRows - zeroCount:
                for i in range(numRows):
                    grid[i][m] ^= 1
        score = 0
        for i in range(numRows):
            for j in range(numCols):
                colScore = grid[i][j] << (numCols - j - 1)

                score += colScore
        return score

