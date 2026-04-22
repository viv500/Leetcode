class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # need to track lowest not highest, since thats the order we look for them in
        max_profit = 0
        lowest = prices[0]

        for price in prices:
            lowest = min(lowest, price)
            max_profit = max(max_profit, price - lowest)

        return max_profit