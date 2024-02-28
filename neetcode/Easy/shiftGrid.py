class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        vLen = len(grid)
        hLen = len(grid[0])
        
        for n in range(0,k):
            print(n)
            lastValue = grid[vLen-1][hLen-1]
            prev = grid[0][0]
            for i in range(vLen):
                for j in range(hLen):
                    temp = grid[i][j]
                    grid[i][j] = prev
                    prev = temp
            grid[0][0] = lastValue
        return grid
