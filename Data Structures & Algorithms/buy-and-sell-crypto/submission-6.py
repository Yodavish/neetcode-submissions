class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = prices[0]
        profit = 0

        for price in prices[1:]:
            result = min(result, price)
            profit = max(profit, price - result)
            
        return profit