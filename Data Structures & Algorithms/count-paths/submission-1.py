class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # Solution 2: Using Tabulation
        
        dp = [[-1] * n for _ in range(m)]
        dp[0][0] = 1        # declaring base case value


        # print(dp)

        for rowNumber in range(m):
            upward = 0
            leftward = 0

            for colNumber in range(n):
                if rowNumber == 0 and colNumber == 0:
                    continue
                if rowNumber > 0:
                    upward = dp[rowNumber - 1][colNumber]
                if colNumber > 0:
                    leftward = dp[rowNumber][colNumber - 1] 

                dp[rowNumber][colNumber] = upward + leftward

        return (dp[m - 1][n - 1])            