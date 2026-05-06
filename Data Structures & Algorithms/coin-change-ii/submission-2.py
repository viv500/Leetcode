class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # only 2 ways to avoid duplicate solutions , 1. dp or 2. index in dfs
        dp = [0] * (amount + 1)
        dp[0] = 1  # 1 way to make amount 0 (choose nothing)

        # coin loop placed outside so that the amount loop starts at coin
        # this means we can reuse coin but can't reuse smaller coins (avoids dupes)
        for coin in coins:
            for a in range(coin, amount + 1):
                dp[a] += dp[a - coin]

        return dp[amount]