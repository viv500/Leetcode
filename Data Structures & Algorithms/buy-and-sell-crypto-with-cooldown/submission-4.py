class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        n = len(prices)

        def dfs(i, holding):
            if i >= n: return 0

            if (i, holding) in dp: return dp[(i, holding)]

            # are we currently holding? can either sell or wait
            if holding:
                sell = prices[i] + dfs(i + 2, False)
                hold = dfs(i + 1, True)
                dp[(i, holding)] = max(sell, hold)
            else:
                # can either buy or wait
                buy = -(prices[i]) + dfs(i + 1, True)
                wait = dfs(i + 1, False) 
                dp[(i, holding)] = max(buy, wait)
            
            return dp[(i, holding)]
        
        return dfs(False, 0)

