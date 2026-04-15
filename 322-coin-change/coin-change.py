class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp : multiple combinations add up to the same sum -> repeated work
        # ex. if we already found min number if coins needed to make $7, and in a future 
        # search we start at $10, reduce the problem to $7 after using a $3 coin, we can now
        # reuse the previously copmuted calculation for $7


        # dp[n] = minimum number of coins needed to sum up to $n
        # = value of each coin + dp[amount - value] i.e. min coins needed to get remaining amount
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for coin in coins:
                if a - coin >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - coin])

        return -1 if dp[amount] == float('inf') else dp[amount]

# DFS + backtracking approach -> TLE
        '''
        minimum_coins = float('inf')

        def dfs(i, coin_set, total):
            nonlocal minimum_coins
            if total > amount or i >= len(coins): return

            if total == amount:
                minimum_coins = min(minimum_coins, len(coin_set))

            # include i
            coin_set.append(coins[i])

            dfs(i, coin_set, total + coins[i])

            coin_set.pop()

            dfs(i + 1, coin_set, total)

        
        dfs(0, [], 0)

        return -1 if minimum_coins == float('inf') else minimum_coins

        '''

        