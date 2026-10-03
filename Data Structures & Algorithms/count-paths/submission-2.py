class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # Solution 3: Space Optimization

        prevRow = [0] * n

        for rowNumber in range(m):
            temp = [0] * n
            for colNumber in range(n):
                if rowNumber == 0 and colNumber == 0:
                    temp[colNumber] = 1
                    continue
                    
                temp[colNumber] = prevRow[colNumber] + temp[colNumber - 1]
            
            prevRow = temp

        return (prevRow[n - 1])            