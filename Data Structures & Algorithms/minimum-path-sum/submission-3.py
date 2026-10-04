class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        # Solution 3: Tabulation + Space Optimization

        row = len(grid)
        col = len(grid[0])

        prev = [0] * col 

        for rowNumber in range(row): 

            current = [0] * col 

            for colNumber in range(col):
            
                # Base case

                # When destination is reached (selecting path)
                if rowNumber == 0 and colNumber == 0:
                    current[colNumber] = grid[rowNumber][colNumber]
                    continue

                # from upward
                upward = float('inf')
                if rowNumber > 0:
                    upward = grid[rowNumber][colNumber] + prev[colNumber]

                # from leftward
                leftward = float('inf')
                if colNumber > 0:
                    leftward = grid[rowNumber][colNumber] + current[colNumber - 1]

                # storing computed value
                current[colNumber] = min(upward, leftward)
            
            prev = current
        
        return prev[col - 1]
