class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prices.reverse()
        maxProfit = 0
        for i in range(len(prices)-1):
            for j in range(i+1, len(prices)):
                profit = prices[i]-prices[j]
                if maxProfit < profit:
                    maxProfit = profit
        return maxProfit
            