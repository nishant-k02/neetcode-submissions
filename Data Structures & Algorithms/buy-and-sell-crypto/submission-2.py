class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        final = []
        if len(prices) == 1:
            return 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                final.append(prices[j] - prices[i])
        if final:
            maxi = max(final)
            if maxi >= 0:
                return maxi
            else:
                return 0