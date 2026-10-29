class Solution:
    def change(self, amount: int, coins: list[int]) -> int:

        # Solution 2: Using Tabulation and memoization
        
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]

        # Base case: one way to make amount 0 (choose no coins)
        for index in range(n + 1):
            dp[index][0] = 1
        
        for index in range(n - 1, -1, -1): 
            for remaining in range(amount + 1):
                
                take = 0
                if remaining >= coins[index]:
                    take = dp[index][remaining - coins[index]]

                notTake = dp[index + 1][remaining]

                dp[index][remaining] = take + notTake
        
        return dp[0][amount]
