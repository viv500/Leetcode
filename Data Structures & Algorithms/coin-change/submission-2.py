class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # greedy (picking largest denom first) DOES NOT work
        # ex. target = 12, coins = [1, 4, 5]
        # greedy: [5, 5, 1, 1], optimal: [4, 4, 4]


        # bottom up DP
        # DP[n] = minimum number of coins needed to amount to n
        # need to bulid up n till amount
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for coin in coins:
                # if coin can even make up the amount
                if a - coin >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - coin])

        return -1 if dp[amount] == float('inf') else dp[amount]





        # BAD brute force DFS + backtracking -> TLE
        self.least = float('inf')
        used = []

        def dfs(i, summ):
            if summ > amount or i == len(coins): return
            if summ == amount:
                self.least = min(self.least, len(used))
                return

            used.append(coins[i])
            dfs(i, summ + coins[i])

            used.pop()
            dfs(i + 1, summ)

        dfs(0, 0)

        return -1 if self.least == float('inf') else self.least 
