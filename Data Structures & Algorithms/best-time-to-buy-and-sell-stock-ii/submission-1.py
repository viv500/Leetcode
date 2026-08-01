class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        self.max_profit = 0
        dp = {}

        def profit(index, holding):
            if index >= len(prices): return 0

            if (index, holding) in dp: return dp[(index, holding)]

            if holding:
                # sell or hold
                dp[(index, holding)] = max(prices[index] + profit(index + 1, False), profit(index + 1, True))
                
            else:
                # buy or skip
                dp[(index, holding)]  = max(profit(index + 1, True) - prices[index], profit(index + 1, False))

            return dp[(index, holding)]
                

        return profit(0, False)

