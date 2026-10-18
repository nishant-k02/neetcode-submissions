from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        ROWS = len(grid)
        COLS = len(grid[0])
        delRow = [-1, 0, 1, 0]
        delCol = [0, 1, 0, -1]
        queue = deque()

        # finding the multi source for entry point (cell will treasure chest i.e 0)
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    queue.append((row, col))
        
        while queue:
            currRow, currCol = queue.popleft()

            # traversing for neighbours -> here 4D traversal only
            for i in range(4):
                nRow = currRow + delRow[i]
                nCol = currCol + delCol[i]

                # check for valid neighbours
                if 0 <= nRow < ROWS and 0 <= nCol < COLS and grid[nRow][nCol] == 2147483647:
                    grid[nRow][nCol] = grid[currRow][currCol] + 1           # updating the distance
                    queue.append((nRow, nCol))          # adding to queue for next traversal
        