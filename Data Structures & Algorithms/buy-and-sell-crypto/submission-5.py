class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Solution 2 - using DP
        maxProfit = 0
        minBuy = prices[0]

        for sell in prices:
            maxProfit = max(maxProfit, sell -  minBuy)
            minBuy =  min(minBuy, sell)
        return maxProfit

        