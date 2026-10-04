class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        # Solution 1: Recursion + Memoization (solves overlapping sub problem)

        row = len(grid)
        col = len(grid[0])

        dp = [[-1] * col for _ in range(row)]

        def recursion(rowNumber, colNumber):

            # Base cases

            # Case 1: When destination is reached (selecting path)
            if rowNumber == 0 and colNumber == 0:
                return grid[0][0]
            
            # Case 2: Exceeds the boundry (not selecting the path)
            if rowNumber < 0 or colNumber < 0:
                return float('inf')
            
            # checking if value is already computed
            if dp[rowNumber][colNumber] != -1:
                return dp[rowNumber][colNumber]

            upward = grid[rowNumber][colNumber] + recursion(rowNumber - 1, colNumber)
            leftward = grid[rowNumber][colNumber] + recursion(rowNumber, colNumber - 1)

            # storing computed value
            dp[rowNumber][colNumber] = min(upward, leftward)

            return dp[rowNumber][colNumber]
        
        return recursion(row - 1, col - 1)
            
