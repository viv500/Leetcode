class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        "can start at index 0 or 1"
        # min cost to get to the ith floor = 
        # min(cost to get to i - 2, cost of i -2, cost to get to i -1, ost of i - 1)
    
        # dp optimization, only need 2 values at a time don't need table
        n = len(cost)
        prev, cur = 0, 0

        for i in range(2, n + 1):
            prev, cur = cur, min(prev + cost[i - 2], cur + cost[i - 1])
            # need to update both at the same time

        return cur

        # !NOTE: if recursion and caching is on dfs(index, cur_total), it'll still TLE cuz theres
        # too many (index, cur_total) combinations to where its not useful to cache
        dp = {} 
        def dfs(index):
            if index in dp: return dp[index]
            if index >= len(cost):
                return 0

            dp[index] = cost[index] + min(dfs(index + 2), dfs(index + 1))

            return dp[index]

        return min(dfs(0), dfs(1))

