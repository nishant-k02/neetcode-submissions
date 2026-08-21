class Solution:
    def solve(self, board: List[List[str]]) -> None:

        rows = len(board)
        cols = len(board[0])
        visitedRegion = [[0 for _ in range(cols)] for _ in range(rows)]

        def dfs(row, col):
            nonlocal visitedRegion, rows, cols

            visitedRegion[row][col] = 1
            delRow = [-1, 0, 1, 0]
            delCol = [0, 1, 0, -1]

            for i in range(4):
                nrow = row + delRow[i]
                ncol = col + delCol[i]

                if 0 <= nrow < rows and 0 <= ncol < cols and visitedRegion[nrow][ncol] == 0 and board[nrow][ncol] == 'O':
                    dfs(nrow, ncol)
        # traverse 1st and last row
        for j in range(cols):
            if board[0][j] == 'O' and visitedRegion[0][j] == 0:
                dfs(0, j)
            
            if board[rows - 1][j] == 'O' and visitedRegion[rows - 1][j] == 0:
                dfs(rows - 1, j)
        
        for i in range(rows):
            # traverse 1st and last column
            if board[i][0] == 'O' and visitedRegion[i][0] == 0:
                dfs(i, 0)
            
            if board[i][cols - 1] == 'O' and visitedRegion[i][cols - 1] == 0:
                dfs(i, cols - 1)

        for i in range(rows):
            for j in range(cols):
                if visitedRegion[i][j] == 0 and board[i][j] == 'O':
                    board[i][j] = 'X'        



        