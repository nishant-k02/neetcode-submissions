class Solution:
    def change(self, amount: int, coins: list[int]) -> int:

        # Solution 1: Using DP, recursion and  memoization

        n = len(coins)
        dp = [[-1] * (amount + 1) for _ in range(n)]
        
        def recursion(index, currSum):
            if currSum == amount:
                return 1
            if index == n or currSum > amount:
                return 0
            
            # checking if value already computed or not before calling any recursion
            if dp[index][currSum] != -1:
                return dp[index][currSum]
            
            take = recursion(index, currSum + coins[index])
            notTake = recursion(index + 1, currSum)
        
            # storing computed values
            dp[index][currSum] = take + notTake

            return dp[index][currSum]
        
        return recursion(0, 0)
