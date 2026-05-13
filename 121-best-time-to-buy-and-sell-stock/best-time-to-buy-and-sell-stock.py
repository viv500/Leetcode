class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_cost = prices[0]
        max_profit = 0
        for price in prices[1:]:
            max_profit = max(max_profit, price - min_cost)
            min_cost = min(min_cost, price)

        return max_profit