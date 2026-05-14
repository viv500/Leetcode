class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        "can start at index 0 or 1"
        # min cost to get to the ith floor = 
        # min(cost to get to i - 2, cost of i -2, cost to get to i -1, ost of i - 1)
    
        # dp optimization, only need 2 values at a time don't need table
        n = len(cost)
        dp = [0] * (n + 1)

        for i in range(2, n + 1):
            dp[i] = min(dp[i - 2] + cost[i - 2], dp[i - 1] + cost[i - 1])

        return dp[n]

