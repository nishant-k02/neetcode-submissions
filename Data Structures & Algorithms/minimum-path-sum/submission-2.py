class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        # Solution 2:  Memoization + Tabulation

        row = len(grid)
        col = len(grid[0])

        dp = [[-1] * col for _ in range(row)]

        for rowNumber in range(row): 
            for colNumber in range(col):

                # Base cases

                # Case 1: When destination is reached (selecting path)
                if rowNumber == 0 and colNumber == 0:
                    dp[rowNumber][colNumber] = grid[rowNumber][colNumber]
                    continue

                # from upward
                upward = float('inf')
                if rowNumber > 0:
                    upward = grid[rowNumber][colNumber] + dp[rowNumber - 1][colNumber]

                # from leftward
                leftward = float('inf')
                if colNumber > 0:
                    leftward = grid[rowNumber][colNumber] + dp[rowNumber][colNumber - 1]

                # storing computed value
                dp[rowNumber][colNumber] = min(upward, leftward)
        
        return dp[row - 1][col - 1]
