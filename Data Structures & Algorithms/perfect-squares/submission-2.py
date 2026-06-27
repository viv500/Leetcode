class Solution:
    def numSquares(self, n: int) -> int:
        # coin change variant
        perfect_squares = []
        number = 1

        # list of all perfect squares less than n
        for i in range(1, n + 1):
            square = i ** 2
            if square > n: break
            perfect_squares.append(square)

        # dp[num] = minimum number of perfect squares needed to sum upto to num
        dp = [float("inf")] * (n + 1)
        dp[0] = 0

        for num in range(1, n + 1):
            for sq in perfect_squares:
                if num >= sq:
                    dp[num] = min(dp[num], 1 + dp[num - sq])

        return dp[n]