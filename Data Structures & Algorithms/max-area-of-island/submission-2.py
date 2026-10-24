from collections import deque
from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        ROWS = len(grid)
        COLS = len(grid[0])
        area = 0
        delRow = [-1, 0, 1, 0]
        delCol = [0, 1, 0, -1]

        queue = deque()

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    queue.append((row, col))
                    grid[row][col] = 0      # marked as visited

                    currArea = 0

                    while queue:
                        currentRow, currentCol = queue.popleft()
                        currArea += 1

                        for i in range(4):
                            nRow = currentRow + delRow[i]
                            nCol = currentCol + delCol[i]

                            if 0 <= nRow < ROWS and 0 <= nCol < COLS and grid[nRow][nCol] == 1:
                                queue.append((nRow, nCol))
                                grid[nRow][nCol] = 0

                    area = max(area, currArea)
        
        return area
 