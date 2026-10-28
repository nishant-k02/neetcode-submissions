class Solution:
    def countServers(self, grid: List[List[int]]) -> int:

        ROWS = len(grid)
        COLS = len(grid[0])
        rowCount = [0] * ROWS
        colCount = [0] * COLS

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    rowCount[row] += 1
                    colCount[col] += 1
        
        result = 0

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] and max(rowCount[row], colCount[col]) > 1:
                    result += 1
        
        return result
