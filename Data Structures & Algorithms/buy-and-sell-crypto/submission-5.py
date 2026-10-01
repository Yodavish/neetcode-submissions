class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0

        result = prices[0]
        profit = {}

        for price in prices[1:]:
            if result > price:
                result = price

            profit[price] = price - result

        if len(profit) > 0:
            return max(profit.values())
        return 0