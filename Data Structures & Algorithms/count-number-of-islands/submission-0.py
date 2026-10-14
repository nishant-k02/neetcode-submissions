from collections import deque
from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        islands = 0
        queue = deque()

        rows = len(grid)
        cols = len(grid[0])

        # finding the entry point i.e a land (cell with 1) which will be the number of islands
        for row in range(rows):
            for col in range(cols):
                # checking if current cell is an islands
                if grid[row][col] == '1':
                    islands += 1
                    queue.append((row, col))        
                    grid[row][col] = '0'        # marking as visited i.e marked as water

                    # array for neighbouring rows and columns (up, right, down, left)
                    delRow = [-1, 0, 1, 0]
                    delCol = [0, 1, 0, -1]

                    while queue:
                        currentRow, currentCol = queue.popleft()

                        # finding the neighbours
                        for index in range(4):      # because only vertical and horizontal movement allowed
                            nRow = currentRow + delRow[index]
                            nCol = currentCol + delCol[index]
    
                            # checking if the neighbouring cell in valid
                            if 0 <= nRow < rows and 0 <= nCol < cols and grid[nRow][nCol] == '1':
                                queue.append((nRow, nCol))
                                grid[nRow][nCol] = '0'      # marking as visited

        return islands  
