class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for i in range(coin, amount + 1):
                target = i - coin
                if target >= 0:
                    dp[i] += dp[target]

        return dp[amount]