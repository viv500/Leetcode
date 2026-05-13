class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        "can buy and sell multiple times -> decision tree/dfs"
        # decion tree:
        # buy or sell or cooldown
        # if buy, then sell or cooldown
        # if sell, then cooldown
        # if cooldown, then buy or sell or cooldown

        # note: we need the holding boolean to tell us what our options are

        dp = {}

        def dfs(index, holding): # holding is true or false
            if index >= len(prices): 
                return 0

            if (index, holding) in dp:
                return dp[(index, holding)]

            cooldown = dfs(index + 1, holding)

            if holding:
                # sell or cooldown 
                buy =  dfs(index + 2, False) + prices[index]  # need to skip a day if sell!
                dp[(index, holding)] = max(buy, cooldown)
            else:
                # buy or cooldown
                sell = dfs(index + 1, True) - prices[index]
                dp[(index, holding)] = max(sell, cooldown)

            
            return dp[(index, holding)]

            
            

        
        return dfs(0, False)


            
