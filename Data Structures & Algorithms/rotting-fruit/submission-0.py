from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        queue = deque()
        visitedArray = [[0 for _ in range(m)] for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
                    visitedArray[i][j] = 2
        maxTime = 0
        delRow = [-1, 0, 1, 0]
        delCol = [0, 1, 0, -1]

        while queue:
            row, col, currTime = queue.popleft()
            maxTime = max(maxTime, currTime)

            for i in range(4):
                nRow = row + delRow[i]
                nCol = col + delCol[i]

                if nRow >= 0 and nRow < n and nCol >= 0 and nCol < m and visitedArray[nRow][nCol] == 0 and grid[nRow][nCol] == 1:
                    queue.append((nRow, nCol, currTime + 1))
                    visitedArray[nRow][nCol] = 2
        for i in range(n):
            for j in range(m):
                if visitedArray[i][j] != 2 and grid[i][j] == 1:
                    return -1
        return maxTime


        