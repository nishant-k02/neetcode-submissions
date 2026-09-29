class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1] * (n + 1)
        def recursion(index):
            nonlocal dp
            if index == 0:
                return 1
            if index == 1:
                return 1
            
            if dp[index] != -1:
                return dp[index]
            
            oneStep = recursion(index - 1)
            twoSteps = recursion(index - 2)

            dp[index] = oneStep + twoSteps
            return oneStep + twoSteps
        return recursion(n)
        