class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # recusrive dfs works but is not efficient enough due to repeated calculations

        dp = [[0] * n for _ in range(m)]

        # base case
        dp[m - 1][n - 1] = 1

        for row in range(m - 1, -1, -1):
            for col in range(n - 1, -1, -1):
                if row + 1 < m: dp[row][col] += dp[row + 1][col]
                if col + 1 < n: dp[row][col] += dp[row][col + 1]

        return dp[0][0]
